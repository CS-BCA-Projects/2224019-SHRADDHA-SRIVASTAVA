from django.shortcuts import render, redirect
from bson.objectid import ObjectId
from django.conf import settings
from pymongo import MongoClient

# Initialize MongoDB Connection
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "securepass123"

# ✅ Admin login required decorator
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("is_admin"):
            return redirect("custom_admin_login")
        return view_func(request, *args, **kwargs)
    return wrapper

# 🔹 Custom Admin Dashboard Homepage
@admin_required
def custom_admin_dashboard(request):  # ✅ Renamed from admin_home
    return render(request, 'admin_home.html')

# 🔹 List of Contacts
@admin_required
def contact_list(request):
    contacts = db["contact"].find()
    contact_list = [{"id": str(contact["_id"]), **contact} for contact in contacts]
    return render(request, 'contact_list.html', {'contacts': contact_list})

# 🔹 Delete Contact
@admin_required
def delete_contact(request, contact_id):
    db["contact"].delete_one({'_id': ObjectId(contact_id)})  # ✅ Fixed query
    return redirect('contact_list')

# 🔹 List of Users
@admin_required
def user_list(request):
    users = db["user"].find()
    user_list = [{"id": str(user["_id"]), **user} for user in users]
    return render(request, 'user_list.html', {'users': user_list})

# 🔹 Delete User
@admin_required
def delete_user(request, user_id):
    db["user"].delete_one({'_id': ObjectId(user_id)})
    return redirect('user_list')

# 🔹 Custom Admin Login Page
def custom_admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session["is_admin"] = True
            return redirect("mongo_admin_home")  # ✅ Fixed redirect
        else:
            return render(request, "custom_admin_login.html", {"error": "Invalid Credentials!"})

    return render(request, "custom_admin_login.html")

# 🔹 Logout Admin
def custom_admin_logout(request):
    request.session.flush()
    return redirect("custom_admin_login")

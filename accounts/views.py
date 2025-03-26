from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.conf import settings
import bcrypt
from django.contrib import messages

# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client["stree_sewa_satkar"]
user_collection = db["user"]

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not name or not phone or not password or not confirm_password:
            return render(request, 'register.html', {'error': "All fields are required."})

        if password != confirm_password:
            return render(request, 'register.html', {'error': "Passwords do not match."})

        if user_collection.find_one({"phone": phone}):
            messages.error(request, "Phone number already registered.")
            return redirect("register")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user_collection.insert_one({
            "name": name,
            "phone": phone,
            "password": hashed_password.decode('utf-8')  
        })

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        user_data = user_collection.find_one({"phone": phone})

        if not user_data:
            messages.error(request, "Invalid phone number.")  # ✅ Show message if phone not found
            return redirect("login")

        stored_password = user_data.get("password")  # Ensure password exists

        if stored_password and bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):  
            request.session["user_id"] = str(user_data["_id"])  
            request.session["user_name"] = user_data["name"]  
            messages.success(request, "Login successful!")
            return redirect("index")  

        messages.error(request, "Invalid password.")  # ✅ Show specific message for wrong password
        return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()  
    messages.success(request, "You have been logged out.")
    return redirect("login")



# from django.shortcuts import render, redirect
# from .forms import RegistrationForm,  LoginForm
# from pymongo import MongoClient
# from django.contrib.auth.hashers import make_password, check_password
# from django.http import JsonResponse
# from django.conf import settings
# import bcrypt
# from django.contrib import messages 
# from .models import User


# # Connect to MongoDB
# client = MongoClient(settings.MONGO_URI)
# db = client['stree_sewa_satkar']  # Your Django database
# user_collection = db['user']  # Collection where user data is stored

# def register(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         phone = request.POST['phone']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         # Check if passwords match
#         if password != confirm_password:
#             return render(request, 'register.html', {'error': "Passwords do not match"})

#         if db.user.find_one({"phone": phone}):
#             messages.error(request, "Phone already exists!")  # ✅ Store message
#             return redirect("register")  # ✅ Redirect to refresh page

#         # Hash the password before storing it
#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#         # Save the user in MongoDB
#         user_data = {
#             "name": name,
#             "phone": phone,
#             "password": hashed_password.decode('utf-8')  # Store hashed password
#         }
#         user_collection.insert_one(user_data)

#         # Redirect to login after successful registration
#         messages.success(request, "Registration successful! Please log in.")  # ✅ Show success message
#         return redirect("login")

#     return render(request, 'register.html')


# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
        
#         if form.is_valid():
#             phone = form.cleaned_data["phone"]
#             password = form.cleaned_data["password"]
            
#             user_data = User.get_user_by_phone(phone)
              
#             if user_data and check_password(password, user_data.get("password", "")):  # ✅ Validate hashed password
#                 return redirect("index")  # ✅ Redirect to dashboard
#             else:
#                 return render(request, "login.html", {"form": form, "error": "Invalid phone number or password!"})
#     else:
#         form = LoginForm()

#     return render(request, "login.html", {"form": form})



# def logout_view(request):
#     return render(request, "logout.html")











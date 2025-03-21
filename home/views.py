from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
from .models import Contact  # Import the Contact model

def index(request):
    return render(request, "index.html")

def contact(request):
    """Handles the contact form submission and stores data in MongoDB."""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")

        if name and email and phone and desc:
            contact_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "desc": desc,
                "date": datetime.now()
            }
            try:
                Contact.save_contact(contact_data)  # Use the save_contact method
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Database Error: {e}")
        else:
            messages.error(request, "Please fill all fields!")

    return render(request, "contact.html")


# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib import messages
# from datetime import datetime
# from django.conf import settings  # Import settings to access MongoDB collections
# from .models import Contact
# # Get the MongoDB collection for contact


# def index(request):
#     return render(request, 'index.html')

# def contact(request):
#     """Handles the contact form submission and stores data in MongoDB."""
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         desc = request.POST.get("desc")

#         if name and email and phone and desc:
#             contact_data = {
#                 "name": name,
#                 "email": email,
#                 "phone": phone,
#                 "desc": desc,
#                 "date": datetime.now()
#             }
#             try:
#                 Contact.collection.insert_one(contact_data)
#                 messages.success(request, "Your message has been sent successfully!")
#             except Exception as e:
#                 messages.error(request, f"Database Error: {e}")
#         else:
#             messages.error(request, "Please fill all fields!")

#     return render(request, "contact.html")



# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib import messages
# from datetime import datetime
# from django.conf import settings  # Import settings to access MongoDB collections

# # Access the MongoDB collection from settings
# contact_collection = settings.MONGO_COLLECTIONS["contact"]

# def index(request):
#     return render(request, 'index.html')

# def contact(request):
#     """Handles the contact form submission and stores data in MongoDB."""
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         desc = request.POST.get("desc")

#         if name and email and phone and desc:
#             # Create data dictionary
#             contact_data = {
#                 "name": name,
#                 "email": email,
#                 "phone": phone,
#                 "desc": desc,
#                 "date": datetime.today()
#             }
#             # Insert into MongoDB
#             contact_collection.insert_one(contact_data)

#             messages.success(request, "Your message has been sent successfully!")
#         else:
#             messages.error(request, "Please fill all fields!")

#     return render(request, "contact.html")

# def save_contact_message(request):
#     """Saves contact messages via API and returns a JSON response."""
#     if request.method == "POST":
#         data = {
#             "name": request.POST.get("name"),
#             "email": request.POST.get("email"),
#             "message": request.POST.get("message"),
#             "date": datetime.today()
#         }
#         # Insert into MongoDB
#         contact_collection.insert_one(data)

#         return JsonResponse({"status": "success", "message": "Contact saved!"})

#     return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


# from django.shortcuts import render, HttpResponse
# from datetime import datetime
# from home.models import Contact
# from django.contrib import messages
# from pymongo import MongoClient
# from django.http import JsonResponse

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')
#     #return HttpResponse("this is homepage")



# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         desc = request.POST.get('desc')
#         contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
#         contact.save()
#         if name and email and phone and desc:
#             # Add success message
#             messages.success(request, "Your message has been sent successfully!")
#         else:
#             # Add error message
#             messages.error(request, "Please fill all fields!")

#     return render(request, 'contact.html')





# def save_contact_message(request):
#     if request.method == "POST":
#         mongo_client = MongoClient()
#         contact_collection = mongo_client.get_collection("contact")

#         data = {
#             "name": request.POST.get("name"),
#             "email": request.POST.get("email"),
#             "message": request.POST.get("message"),
#         }
#         contact_collection.insert_one(data)
#         return JsonResponse({"status": "success", "message": "Contact saved!"})

        


  

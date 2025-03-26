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


        


  

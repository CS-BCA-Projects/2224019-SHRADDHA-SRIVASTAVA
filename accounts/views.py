from django.shortcuts import render, redirect
from .forms import RegistrationForm,  LoginForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse




def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_data = {
                "name": form.cleaned_data["name"],
                "phone": form.cleaned_data["phone"],
                "age": form.cleaned_data["age"],
                "menstruation_duration": form.cleaned_data["menstruation_duration"],
                "menstrual_flow": form.cleaned_data["menstrual_flow"],
                "skin_type": form.cleaned_data["skin_type"],
                "itchiness": form.cleaned_data["itchiness"],
                "password": make_password(form.cleaned_data["password"]),  # Hash password
            }
            form.cleaned_data.pop("confirm_password", None) 

            User.register_user(user_data)
            return redirect("dashboard", phone=user_data["phone"])  # Redirect to dashboard

    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            
            user_data = User.get_user_by_phone(phone)
              
            if user_data and check_password(password, user_data.get("password", "")):  # ✅ Validate hashed password
                return redirect("dashboard", phone=user_data["phone"])  # ✅ Redirect to dashboard
            else:
                return render(request, "login.html", {"form": form, "error": "Invalid phone number or password!"})
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})






def dashboard(request, phone):
    user = User.get_user_by_phone(phone)
    
    # Recommend pad based on skin type
    recommendations = {
        "Dry": "Soft Cotton Pads",
        "Oily": "Ultra-Thin Breathable Pads",
        "Normal": "Regular Absorbent Pads",
        "Sensitive": "Breathable pads",
        "Combination": "Natural pads"
    }
    
    recommended_pad = recommendations.get(user["skin_type"], "Regular Pads")

    return render(request, "dashboard.html", {"user": user, "recommended_pad": recommended_pad})





# Logout View
def logout_view(request):
    return render(request, "logout.html")











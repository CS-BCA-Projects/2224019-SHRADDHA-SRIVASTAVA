from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import QuestionnaireForm
from pymongo import MongoClient
from django.conf import settings
import datetime

# MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI if using a remote MongoDB
# db = client['stree_seva_satkar']  # Database name
# result_collection = db['result']  # Collection name

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
result_collection = db["result"]


def questionnaire_view(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            data = {
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'duration': form.cleaned_data['duration'],
                'flow': form.cleaned_data['flow'],
                'skin_type': form.cleaned_data['skin_type'],
                'itchiness': form.cleaned_data['itchiness'],
            }
            
            # Store the data in MongoDB "result" collection
            result_collection.insert_one(data)
            
            # Redirect to dashboard with skin_type
            skin_type = form.cleaned_data['skin_type']
            return redirect(reverse('dashboard', args=[skin_type]))
        else:
            # Print errors to console for debugging
            print(form.errors)
    else:
        form = QuestionnaireForm()

    return render(request, 'questionnaire.html', {'form': form})

def dashboard_view(request, skin_type):
    # Optionally fetch data from MongoDB for display on the dashboard
    result_data = result_collection.find_one({'skin_type': skin_type})  # Get the latest entry
    return render(request, 'dashboard.html', {'skin_type': skin_type, 'result_data': result_data})

# from django.shortcuts import render, redirect
# from .forms import QuestionnaireForm

# def questionnaire_view(request):
#     if request.method == "POST":
#         form = QuestionnaireForm(request.POST)
#         if form.is_valid():
#             skin_type = form.cleaned_data["skin_type"]  # Get skin type from the form
#             return redirect("dashboard", skin_type=skin_type)  # Redirect to dashboard
#     else:
#         form = QuestionnaireForm()
    
#     return render(request, "questionnaire.html", {"form": form})

# def dashboard(request, skin_type):
#     # Recommend pad based on skin type
#     recommendations = {
#         "Dry": "Soft Cotton Pads",
#         "Oily": "Ultra-Thin Breathable Pads",
#         "Normal": "Regular Absorbent Pads",
#         "Sensitive": "Breathable Pads",
#         "Combination": "Natural Pads",
#     }
    
#     recommended_pad = recommendations.get(skin_type, "Regular Pads")

#     return render(request, "dashboard.html", {"skin_type": skin_type, "recommended_pad": recommended_pad})





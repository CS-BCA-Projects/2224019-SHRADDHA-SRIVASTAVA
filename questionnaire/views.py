from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.conf import settings
from django.contrib import messages

# MongoDB connection
client = MongoClient(settings.MONGO_URI)
db = client["stree_sewa_satkar"]
result_collection = db["result"]

def questionnaire(request):
    if request.method == "POST":
        user_name = request.session.get('user_name')
        if not user_name:
            messages.error(request, "Please log in to submit the questionnaire.")
            return redirect('login')

        age = request.POST.get('age')
        duration = request.POST.get('duration')
        flow = request.POST.get('flow')
        skin_type = request.POST.get('skin_type')
        itchiness = request.POST.get('itchiness')

        result_data = {
            'name': user_name,
            'age': int(age),
            'duration': duration,
            'flow': flow,
            'skin_type': skin_type,
            'itchiness': itchiness
        }
        result_collection.update_one({'name': user_name}, {'$set': result_data}, upsert=True)

        # Update profile immediately after submission
        from myself.views import save_profile_data
        save_profile_data(user_name)

        return redirect('dashboard', skin_type=skin_type)

    return render(request, 'questionnaire.html')

def dashboard(request, skin_type):
    user_name = request.session.get('user_name')
    if not user_name:
        messages.error(request, "Please log in to view the dashboard.")
        return redirect('login')

    result_data = result_collection.find_one({'name': user_name})
    return render(request, 'dashboard.html', {'skin_type': skin_type, 'result_data': result_data})


# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .forms import QuestionnaireForm
# from pymongo import MongoClient
# from django.conf import settings
# import datetime

# # MongoDB connection
# # client = MongoClient('mongodb://localhost:27017/')  # Adjust the URI if using a remote MongoDB
# # db = client['stree_seva_satkar']  # Database name
# # result_collection = db['result']  # Collection name

# client = MongoClient(settings.MONGO_URI)
# db = client[settings.MONGO_DB_NAME]
# result_collection = db["result"]


# def questionnaire_view(request):
#     if request.method == 'POST':
#         user_name = request.session.get('user_name')
#         if not user_name:
            
#         form = QuestionnaireForm(request.POST)
#         if form.is_valid():
#             # Extract cleaned data from the form
#             data = {
#                 'name': form.cleaned_data['name'],
#                 'age': form.cleaned_data['age'],
#                 'duration': form.cleaned_data['duration'],
#                 'flow': form.cleaned_data['flow'],
#                 'skin_type': form.cleaned_data['skin_type'],
#                 'itchiness': form.cleaned_data['itchiness'],
#             }
            
#             # Store the data in MongoDB "result" collection
#             result_collection.insert_one(data)
            
#             # Redirect to dashboard with skin_type
#             skin_type = form.cleaned_data['skin_type']
#             return redirect(reverse('dashboard', args=[skin_type]))
#         else:
#             # Print errors to console for debugging
#             print(form.errors)
#     else:
#         form = QuestionnaireForm()

#     return render(request, 'questionnaire.html', {'form': form})

# def dashboard_view(request, skin_type):
#     # Optionally fetch data from MongoDB for display on the dashboard
#     result_data = result_collection.find_one({'skin_type': skin_type})  # Get the latest entry
#     return render(request, 'dashboard.html', {'skin_type': skin_type, 'result_data': result_data})






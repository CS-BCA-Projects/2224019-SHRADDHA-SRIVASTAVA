from django.shortcuts import render, redirect
from pymongo import MongoClient
from django.conf import settings
from django.contrib import messages

# MongoDB connection
client = MongoClient(settings.MONGO_URI)
db = client["stree_sewa_satkar"]
user_collection = db["user"]
result_collection = db["result"]
profile_collection = db["profile"]

def save_profile_data(user_name):
    """Save user and result data to profile collection."""
    user_data = user_collection.find_one({'name': user_name})
    result_data = result_collection.find_one({'name': user_name})
    
    profile_data = {
        'name': user_data.get('name'),
        'phone': user_data.get('phone'),
    }
 
    if result_data:
        profile_data.update({
            'age': result_data.get('age'),
            'duration': result_data.get('duration'),
            'flow': result_data.get('flow'),
            'skin_type': result_data.get('skin_type'),
            'itchiness': result_data.get('itchiness'),
        })
    
    profile_collection.update_one({'name': user_name}, {'$set': profile_data}, upsert=True)

def index(request):
    user_name = request.session.get('user_name')
    profile_data = profile_collection.find_one({'name': user_name}) if user_name else None
    return render(request, 'index.html', {'profile_data': profile_data})

def profile(request):
    user_name = request.session.get('user_name')
    if not user_name:
        messages.error(request, "Please log in to view your profile.")
        return redirect('login')

    profile_data = profile_collection.find_one({'name': user_name})

    if not profile_data:
        messages.error(request, "Profile data not found. Please register and submit the questionnaire.")
        return render(request, 'profile.html', {'profile_data': None})

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'edit':
            updated_profile_data = {
                'name': request.POST.get('name'),
                'phone': profile_data.get('phone'),
                'age': int(request.POST.get('age')) if request.POST.get('age') else profile_data.get('age'),
                'duration': request.POST.get('duration') if request.POST.get('duration') else profile_data.get('duration'),
                'flow': request.POST.get('flow') if request.POST.get('flow') else profile_data.get('flow'),
                'skin_type': request.POST.get('skin_type') if request.POST.get('skin_type') else profile_data.get('skin_type'),
                'itchiness': request.POST.get('itchiness') if request.POST.get('itchiness') else profile_data.get('itchiness'),
            }
            profile_collection.update_one({'name': user_name}, {'$set': updated_profile_data})
            user_collection.update_one({'name': user_name}, {'$set': {'name': updated_profile_data['name']}})
            if result_collection.find_one({'name': user_name}):
                result_collection.update_one({'name': user_name}, {'$set': updated_profile_data})
            messages.success(request, "Profile updated successfully!")
            profile_data = updated_profile_data

        elif action == 'delete':
            profile_collection.delete_one({'name': user_name})
            user_collection.delete_one({'name': user_name})
            if result_collection.find_one({'name': user_name}):
                result_collection.delete_one({'name': user_name})
            messages.success(request, "Profile deleted successfully!")
            request.session.flush()
            return redirect('login')

    return render(request, 'profile.html', {'profile_data': profile_data})

def logout(request):
    user_name = request.session.get('user_name')
    if user_name:
        profile_collection.delete_one({'name': user_name})
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('login')
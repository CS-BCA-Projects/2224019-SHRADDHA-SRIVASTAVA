from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.contrib.auth import logout

@login_required
def profile_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found. Please complete the questionnaire.')
        return redirect('questionnaire')
    
    context = {
        'username': request.user.username,
        'email': request.user.email,
        'duration': profile.duration,
        'flow': profile.flow,
        'skin_type': profile.skin_type,
        'itchiness': profile.itchiness,
    }
    return render(request, 'myself/profile.html', context)

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.duration = request.POST.get('duration')
        profile.flow = request.POST.get('flow')
        profile.skin_type = request.POST.get('skin_type')
        profile.itchiness = request.POST.get('itchiness')
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'myself/profile.html', {
        'profile': profile,
        'edit_mode': True
    })

@login_required
def delete_profile(request):
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(user=request.user)
            profile.delete()
            user = request.user
            user.delete()  # Deletes the user from the User collection
            logout(request)
            messages.success(request, 'Profile and account deleted successfully!')
            return redirect('login')  # Assuming 'login' is defined in accounts app
        except Profile.DoesNotExist:
            messages.error(request, 'Profile not found.')
    return redirect('profile')

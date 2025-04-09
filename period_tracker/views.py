from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PeriodTracker
from .forms import PeriodTrackerForm
from datetime import datetime, timedelta
from twilio.rest import Client
from django.conf import settings
import random
from twilio.base.exceptions import TwilioRestException

def tracker_form(request):
    user_name = request.session.get('user_name')

    if not user_name:
        messages.error(request, "Please login first to use the Period Tracker feature.")
        return redirect('login')

    # Load existing tracker data for the user, if any
    tracker = PeriodTracker.get_tracker(user_name)
    initial_data = tracker if tracker else {}

    if request.method == 'POST':
        print("📍 POST request received in tracker_for")

        form = PeriodTrackerForm(request.POST)
        if form.is_valid():
            last_period_date = form.cleaned_data['last_period_date'].strftime("%Y-%m-%d")
            cycle_length = form.cleaned_data['cycle_length']
            phone_number = form.cleaned_data['phone_number']
            sms_enabled = form.cleaned_data['sms_enabled']
            mood = form.cleaned_data.get('mood')
            water_intake = form.cleaned_data.get('water_intake')
            cravings = form.cleaned_data.get('cravings')

            # Save the data to MongoDB
            PeriodTracker.create_or_update(
                user_name=user_name,
                last_period_date=last_period_date,
                cycle_length=cycle_length,
                phone_number=phone_number,
                sms_enabled=sms_enabled,
                mood=mood,
                water_intake=water_intake,
                cravings=cravings
            )

            # Send SMS confirmation if enabled
            if sms_enabled and phone_number:
                try:
                    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
                    next_period = PeriodTracker.calculate_next_period(last_period_date, cycle_length)

                    # Motivational Quotes
                    quotes = [
                        "Stay strong, you are amazing! 💖",
                        "Your health is your wealth, take care of yourself! 🌸",
                        "You are more powerful than you think! 💪",
                        "Hydrate, nourish, and be kind to yourself! 💧",
                        "You are doing great! Keep going. 🌟"
                    ]
                    quote_message = random.choice(quotes)

                    message = f"Hi {user_name}, hope you're doing well! 💕 Your next period is expected on {next_period}. {quote_message}"

                    client.messages.create(
                        body=message,
                        from_=settings.TWILIO_PHONE,
                        to=f"+91{phone_number}" if not phone_number.startswith("+") else phone_number
                    )

                    messages.success(request, "Tracking details saved and SMS sent successfully! 📩")

                except TwilioRestException as e:
                    messages.warning(request, f"Tracking details saved, but SMS failed: {str(e)}")
            else:
                messages.success(request, "Tracking details saved successfully! ✅")

            # Reload the form with prefilled values
            form = PeriodTrackerForm(initial={
                'last_period_date': last_period_date,
                'cycle_length': cycle_length,
                'phone_number': phone_number,
                'sms_enabled': sms_enabled,
                'mood': mood,
                'water_intake': water_intake,
                'cravings': cravings,
            })

    else:
        form = PeriodTrackerForm(initial=initial_data)

    return render(request, 'tracker_form.html', {
    'form': form,
    'form_errors': form.errors if request.method == 'POST' else None
     })


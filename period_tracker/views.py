# project_tracker/views.py
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

    tracker = PeriodTracker.get_tracker(user_name)
    initial_data = tracker if tracker else {}

    if request.method == 'POST':
        form = PeriodTrackerForm(request.POST)
        if form.is_valid():
            last_period_date = form.cleaned_data['last_period_date'].strftime("%Y-%m-%d")
            cycle_length = form.cleaned_data['cycle_length']
            phone_number = form.cleaned_data['phone_number']
            sms_enabled = form.cleaned_data['sms_enabled']

            # Save the data to MongoDB
            PeriodTracker.create_or_update(
                user_name=user_name,
                last_period_date=last_period_date,
                cycle_length=cycle_length,
                phone_number=phone_number,
                sms_enabled=sms_enabled
            )

            # Send SMS confirmation if enabled
            if sms_enabled and phone_number:
                try:
                    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
                    next_period = PeriodTracker.calculate_next_period(last_period_date, cycle_length)

                    # Motivational Messages
                    quotes = [
                        "Stay strong, you are amazing! 💖",
                        "Your health is your wealth, take care of yourself! 🌸",
                        "You are more powerful than you think! 💪",
                        "Hydrate, nourish, and be kind to yourself! 💧",
                        "You are doing great! Keep going. 🌟"
                    ]
                    quote_message = random.choice(quotes)

                    # SMS Message
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

            # ✅ Instead of redirecting, reload the form with a success message
            form = PeriodTrackerForm(initial={
                'last_period_date': last_period_date,
                'cycle_length': cycle_length,
                'phone_number': phone_number,
                'sms_enabled': sms_enabled
            })

    else:
        form = PeriodTrackerForm(initial=initial_data)

    return render(request, 'tracker_form.html', {'form': form})  # ✅ Render the form instead of redirecting


def send_period_reminders():
    """Send SMS reminders to users whose periods are approaching."""
    upcoming_date = (datetime.today() + timedelta(days=3)).strftime("%Y-%m-%d")
    trackers = PeriodTracker.get_all_trackers_with_sms()
    
    client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
    for tracker in trackers:
        next_period = PeriodTracker.calculate_next_period(tracker['last_period_date'], tracker['cycle_length'])
        if next_period == upcoming_date:
            try:
                message = f"Reminder: Your next period is expected on {next_period}. Stay prepared!"
                response = client.messages.create(
                    body=message,
                    from_=settings.TWILIO_PHONE,
                    to=tracker['phone_number']
                )
                print(f"SMS sent to {tracker['phone_number']} for period on {next_period}. Message SID: {response.sid}")
            except TwilioRestException as e:
                print(f"Failed to send SMS to {tracker['phone_number']}: {str(e)} (Error Code: {e.code})")
                continue
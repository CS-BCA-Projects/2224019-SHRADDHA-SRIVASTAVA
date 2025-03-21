from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai import get_gemini_response
from .models import Chatbot

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()

        if not user_message:
            return JsonResponse({"response": "Please enter a message!"})

        ai_response = get_gemini_response(user_message)

        # Save chat history
        Chatbot.save_message("User", user_message, ai_response)

        return JsonResponse({"message": user_message, "response": ai_response})

    return render(request, "chatbot.html")
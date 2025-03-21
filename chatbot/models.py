from pymongo import MongoClient
from django.conf import settings




class Chatbot:

    collection = settings.MONGO_COLLECTIONS["response"] 
    
    @staticmethod
    def save_message(user, user_message, bot_response):
        chat_entry = {
            "user": user,
            "user_message": user_message,
            "bot_response": bot_response
        }
        Chatbot.collection.insert_one(chat_entry)
    
    @staticmethod
    def get_all_messages():
        return list(Chatbot.collection.find({}, {"_id": 0}))




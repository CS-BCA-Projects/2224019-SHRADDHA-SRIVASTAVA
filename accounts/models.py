from pymongo import MongoClient
from django.conf import settings
import bcrypt

# Connect to MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
user_collection = db["user"]

class User:
    """A class to handle user operations in MongoDB."""

    @staticmethod
    def create_user(name, phone, password):
        """Registers a new user in MongoDB with a hashed password."""
        if user_collection.find_one({"phone": phone}):
            return False  # User already exists
        
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        user_collection.insert_one({
            "name": name,
            "phone": phone,
            "password": hashed_password.decode("utf-8")  
        })
        return True  # Registration successful

    @staticmethod
    def get_user_by_phone(phone):
        """Fetches a user by phone number."""
        return user_collection.find_one({"phone": phone})

    @staticmethod
    def authenticate(phone, password):
        """Checks if the provided phone and password are correct."""
        user = user_collection.find_one({"phone": phone})
        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            return user  
        return None  





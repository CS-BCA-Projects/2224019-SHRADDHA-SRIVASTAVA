# from django.db import models
from django.db import models

from django.conf import settings
from django.contrib.auth.hashers import check_password
# Correcting database connection
# ✅ Use correct setting name


# Access MongoDB
# db = settings.db

class User:
    collection = settings.MONGO_COLLECTIONS["user"] # MongoDB collection

    @staticmethod
    def register_user(data):
        """Insert user data into MongoDB."""
        User.collection.insert_one(data)

    @staticmethod
    def get_user_by_phone(phone):
        """Retrieve user data by phone number."""
        return User.collection.find_one({"phone": phone})


# Create your models here.

    @staticmethod
    def authenticate(phone, password):
        """Check if user exists and verify password."""
        user = User.collection.find_one({"phone": phone})
        if user and check_password(password, user.get["password"]):  
           return User
        return None


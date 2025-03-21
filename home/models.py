from django.conf import settings

class Contact:
    collection = settings.MONGO_COLLECTIONS["contact"]

    @staticmethod
    def save_contact(data):
        """Save contact form data."""
        Contact.collection.insert_one(data)

    @staticmethod
    def get_all_contacts():
        """Retrieve all contacts."""
        return list(Contact.collection.find({}))


# from django.db import models
# from django.conf import settings


# class Contact:
#     collection = settings.MONGO_COLLECTIONS["contact"]

#     @staticmethod
#     def save_contact(data):
#         """Save contact form data."""
#         Contact.collection.insert_one(data)

#     @staticmethod
#     def get_all_contacts():
#         """Retrieve all contacts."""
#         return list(Contact.collection.find({}))





# #Create your models here.
# class Contact(models.Model):
#      name = models.CharField(max_length=122)
#      email = models.CharField(max_length=122)
#      phone = models.CharField(max_length=12)
#      desc = models.TextField(null=True, blank=True)
#      date = models.DateField()

#      def __str__(self):
#         return self.name


# from djongo import models
# from pymongo import MongoClient
# from django.conf import settings

# # Correcting database connection
# client = MongoClient(settings.MONGO_URI)  # ✅ Correct way
# db = client[settings.MONGO_DB_NAME] # ✅ Use correct setting name


# # Access MongoDB
# # db = settings.db
# class User:
#     collection = db["contact"] 
# # Create your models here.
# class Contact(models.Model):
#     name = models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     phone = models.CharField(max_length=12)
#     desc = models.TextField(null=True, blank=True)
#     date = models.DateField()

#     def __str__(self):
#         return self.name




from django.contrib import admin



# from django.contrib import admin
# from django.http import HttpResponse
# from django.urls import path
# from django.shortcuts import render
# from .models import User

# class UserAdmin:
#     """Custom admin panel for managing users stored in MongoDB."""

#     def user_list(request):
#         """Retrieve and display all users from MongoDB."""
#         users = list(User.collection.find({}))
#         return render(request, "admin_users.html", {"users": users})

#     def delete_user(request, phone):
#         """Delete a user from MongoDB."""
#         User.collection.delete_one({"phone": phone})
#         return HttpResponse("User deleted successfully! <a href='/admin/users/'>Go Back</a>")

# # Custom admin URL patterns
# def get_admin_urls():
#     return [
#         path("users/", UserAdmin.user_list, name="user_list"),
#         path("delete_user/<str:phone>/", UserAdmin.delete_user, name="delete_user"),
#     ]
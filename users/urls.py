from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('register/', registerUser, name='register'),
    path('logout/', custom_logout, name='logout'),
]

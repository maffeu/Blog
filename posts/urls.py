from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list, name="postList"),
    path('<int:pk>', post_details, name="details"),
    path('delete/<int:pk>', deletePost, name='deletePost'),
    path('update/<int:pk>', updatePost, name='updatePost'),

]

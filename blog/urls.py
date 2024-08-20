
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact',contact, name="contact-us"),
    path('posts/', include('posts.urls')),
    # path('news/<int:id>', news, name="news-page"),
    path('accounts/', include('users.urls'), name='accounts')
]


# CRUD
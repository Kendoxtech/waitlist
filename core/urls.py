# waitlist/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='waitlist_home'),
    path('submit/', views.submit_waitlist, name='submit_waitlist'),
]

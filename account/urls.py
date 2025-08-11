from django.urls import path
from .views import *

urlpatterns = [
    path('about/',view.about_page,name='about_account'),
]
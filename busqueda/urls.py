from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('category', category),
    path('search', search)

]

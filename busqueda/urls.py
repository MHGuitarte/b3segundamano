from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='inicio'),
    path('category', category),
    path('search', search)

]

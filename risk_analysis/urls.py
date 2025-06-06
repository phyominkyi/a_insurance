# myapp/urls.py
# risk_analysis/Fire/earthquake_paril/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.earthquake_home, name='earthquake_home'),
]

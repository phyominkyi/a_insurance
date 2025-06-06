# risk_analysis/Fire/earthquake_paril/views.py

from django.shortcuts import render

def earthquake_home(request):
    return render(request, 'earthquake_paril/index.html')

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'training_resources/new_teammate_training.html')

def anatomy_fundamentals(request):
    return render(request, 'training_resources/anatomy_fundamentals.html')

def cardiac_surgical_intervention(request):
    return render(request, 'training_resources/cardiac_surgical_intervention.html')
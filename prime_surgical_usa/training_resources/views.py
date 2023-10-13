from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def index(request):
    return render(request, 'training_resources/new_teammate_training.html')

#@login_required
def anatomy_fundamentals(request):
    return render(request, 'training_resources/anatomy_fundamentals.html')

#@login_required
def cardiac_surgical_intervention(request):
    return render(request, 'training_resources/cardiac_surgical_intervention.html')
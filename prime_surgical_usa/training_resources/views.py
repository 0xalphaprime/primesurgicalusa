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

def zb_cv_portfolio(request):
    return render(request, 'training_resources/zimmer_biomet_cv_sternal.html')

def intro_videos(request):
    return render(request, 'training_resources/anatomy_videos.html')

def zb_slb_portfolio(request):
    return render(request, 'training_resources/zb_slb.html')

def zb_ez_portfolio(request):
    return render(request, 'training_resources/zb_ez.html')

def zb_360_portfolio(request):
    return render(request, 'training_resources/zb_360.html')

def zb_xp_portfolio(request):
    return render(request, 'training_resources/zb_xp.html')

def zb_wire_cable_portfolio(request):
    return render(request, 'training_resources/zb_wires_and_cables.html')
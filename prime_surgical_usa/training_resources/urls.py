from django.urls import path

from . import views

app_name = "training_resources"

urlpatterns = [
    path("", views.index, name="training"),
    path("heart/", views.anatomy_fundamentals, name="heart"),
    path("surgery/", views.cardiac_surgical_intervention, name="surgery"),

]
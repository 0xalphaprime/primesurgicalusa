from django.urls import path


from . import views

app_name = "training_resources"

urlpatterns = [
    path("", views.index, name="training"),
    path("heart/", views.anatomy_fundamentals, name="heart"),
    path("surgery/", views.cardiac_surgical_intervention, name="surgery"),
    path("zbcv/", views.zb_cv_portfolio, name="zbcv"),
    path("videos/", views.intro_videos, name="videos"),
    path("zbslb/", views.zb_slb_portfolio, name="zbslb"),
    path("zbez/", views.zb_ez_portfolio, name="zbez"),
    path("zb360/", views.zb_360_portfolio, name="zb360"),
    path("zbxp/", views.zb_xp_portfolio, name="zbxp"),
    path("zbwires/", views.zb_wire_cable_portfolio, name="zbwires")
]
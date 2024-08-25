from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "training_resources"

urlpatterns = [
    path("", views.index, name="training"),
    path("heart/", RedirectView.as_view(url='https://literate-geography-48e.notion.site/1-Foundational-Anatomy-482b5a67d93d4acbaa26b05f0688f629'), name="heart"),
    path("surgery/", views.cardiac_surgical_intervention, name="surgery"),
    path("zbcv/", views.zb_cv_portfolio, name="zbcv"),
    path("videos/", views.intro_videos, name="videos"),
    path("zbslb/", views.zb_slb_portfolio, name="zbslb"),
    path("zbez/", views.zb_ez_portfolio, name="zbez"),
    path("zb360/", views.zb_360_portfolio, name="zb360"),
    path("zbxp/", views.zb_xp_portfolio, name="zbxp"),
    path("zbwires/", views.zb_wire_cable_portfolio, name="zbwires"),
    path("zbrfssrf/", views.zb_rf_ssrf_portfolio, name="zbrfssrf"),
    path("zbrfadvantage/", views.zb_ssrf_advantage, name="zbrfadvantage"),
    path("zbrfblu/", views.zb_ssrf_blu, name="zbrfblu"),
]
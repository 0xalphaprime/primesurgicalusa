from django.urls import path


from . import views

app_name = "sales_performance"

urlpatterns = [
    path("", views.index, name="sales"),
    path("zb/", views.zb_sales_dashboard, name="zb"),
]
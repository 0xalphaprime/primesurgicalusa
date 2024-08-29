from django.urls import path


from . import views

app_name = "sales_performance"

urlpatterns = [
    path("", views.index, name="sales"),
    path("zb_sheets_data/", views.sheet_data_view, name="zb_sheets_data"),
]
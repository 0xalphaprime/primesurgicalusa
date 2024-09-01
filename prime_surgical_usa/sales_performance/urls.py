from django.urls import path


from . import views

app_name = "sales_performance"

urlpatterns = [
    path("", views.index, name="sales"),
    path("zb_sheets_data/", views.sheet_data_view, name="zb_sheets_data"),
    path('item-class-rolling-qtr/', views.item_class_rolling_qtr, name='item_class_rolling_qtr'),
    path('rolling-month-customer/', views.rolling_month_customer, name='rolling_month_customer'),
]
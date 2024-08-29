from django.shortcuts import render
from .gsheets import get_google_sheet_data  # Import the function that pulls data from Google Sheets


# Create your views here.

def sheet_data_view(request):
    # Fetch the data from Google Sheets
    data = get_google_sheet_data()

    # Pass the data to the template context
    return render(request, 'sales_performance\zb_sales_dash.html', {'data': data})

def index(request):
    return render(request, 'sales_performance/sales_performance.html')

def zb_sales_dashboard(request):
    return render(request, 'sales_performance/zb_sales_dash.html')
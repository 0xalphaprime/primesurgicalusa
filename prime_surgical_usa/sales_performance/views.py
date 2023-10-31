from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sales_performance/sales_performance.html')

def zb_sales_dashboard(request):
    return render(request, 'sales_performance/zb_sales_dash.html')
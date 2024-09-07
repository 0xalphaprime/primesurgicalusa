# pricing_search/views.py
from django.shortcuts import render
from django.db.models import Avg, Min, Max
from .models import PriceRecord

def search_view(request):
    item_number = request.GET.get('item_number', None)
    records = []

    if item_number:
        records = PriceRecord.objects.filter(item_number=item_number)
        summary = records.aggregate(
            avg_price=Avg('price'),
            min_price=Min('price'),
            max_price=Max('price')
        )
    else:
        summary = {}

    return render(request, 'pricing_search/search.html', {
        'records': records,
        'summary': summary,
        'item_number': item_number
    })
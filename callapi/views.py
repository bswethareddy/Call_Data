# callapi/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Call
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator

# call_records/views.py
from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')


def initiate_call(request):
    if request.method == 'POST':
        from_number = request.POST.get('from_number')
        to_number = request.POST.get('to_number')

        call_record = Call(from_number=from_number, to_number=to_number)
        call_record.save()

        return JsonResponse({'message': 'Call initiated successfully'})

    return render(request, 'initiate_call.html')

def call_report(request):
    if request.method == 'GET':
        phone_number = request.GET.get('phone')
        call_records = Call.objects.filter(Q(from_number=phone_number) | Q(to_number=phone_number))
        
        paginator = Paginator(call_records, 10)
        
        page_number = request.GET.get('page', 1)
        
        page_records = paginator.get_page(page_number)
        
        context = {
            'phone': phone_number,
            'call_records': page_records,
        }
        
    if request.META.get('HTTP_X_REQUESTD_WITH') == 'XMLHttpRequest':
        return render(request, 'partial_call_report.html', context)
    else:
        return render(request, 'call_report.html', context)

        

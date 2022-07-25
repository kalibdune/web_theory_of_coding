from django.shortcuts import render
from .models import Block_hamming

def hamming_page(request):
    paragrafs = Block_hamming.objects.all().order_by('position')
    return render(request, 'hamming_page.html', {
        'paragrafs': paragrafs
    })

def tasks_page(request):
    return render(request, 'tasks_hamming.html')
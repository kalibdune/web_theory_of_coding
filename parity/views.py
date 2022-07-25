from django.shortcuts import render
from .models import Block_parity

def parity_page(request):
    paragrafs = Block_parity.objects.all().order_by('position')
    return render(request, 'parity_page.html', {
        'paragrafs': paragrafs
    })
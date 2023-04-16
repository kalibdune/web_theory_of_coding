from django.shortcuts import render
from .models import reed_solomon


def reed_solomon_page(request):
    paragrafs = reed_solomon.objects.all().order_by('position')
    return render(request, 'reed_solomon.html', {
        'paragrafs': paragrafs
    })
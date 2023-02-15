from django.shortcuts import render
from .models import Block_hamming, Task

def hamming_page(request):
    paragrafs = Block_hamming.objects.all().order_by('position')
    return render(request, 'hamming_page.html', {
        'paragrafs': paragrafs
    })

def tasks_page(request):
    task2 = Task.objects.all().filter(level=2)
    task3 = Task.objects.all().filter(level=3)
    task5 = Task.objects.all().filter(level=5)
    return render(request, 'tasks_hamming.html', {
        'tasks2': task2,
        'tasks3': task3,
        'tasks5': task5
    })
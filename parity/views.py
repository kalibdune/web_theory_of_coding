from django.shortcuts import render

def parity_page(request):
    return render(request, 'parity_page.html')
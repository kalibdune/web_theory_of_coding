from django.shortcuts import render


def hamming_page(request):
    return render(request, 'hamming_page.html')

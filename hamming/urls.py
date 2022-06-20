from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.hamming_page, name='hamming_page')
]
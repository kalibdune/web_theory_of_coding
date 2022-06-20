from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.parity_page, name='parity_page')
]
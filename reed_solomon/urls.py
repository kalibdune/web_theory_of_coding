from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.reed_solomon_page, name='reed_solomon')
]
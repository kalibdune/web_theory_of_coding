from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.hamming_page, name='hamming_page'),
    path('tasks/', views.tasks_page, name='tasks')
]
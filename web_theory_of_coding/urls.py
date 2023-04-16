from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamming/', include('hamming.urls')),
    path('parity/', include('parity.urls')),
    path('reed_solomon/', include('reed_solomon.urls')),
    path('', include('main.urls'))
]

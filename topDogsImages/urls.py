from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.voting.urls')),
    path('127.0.0.1', include('apps.voting.urls')),
    path('admin/', admin.site.urls),
]

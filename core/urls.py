
from django.contrib import admin


from django.urls import include, path
from rest_framework import routers

from app.authbase import urls

urlpatterns = [
    path('api/', include('app.authbase.urls'), name = 'api'),
    path('admin/', admin.site.urls),
    ]
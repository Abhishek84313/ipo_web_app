from django.contrib import admin
from django.urls import path, include
from ipo_web.views import IPOInfoAPI

urlpatterns = [
    path('',IPOInfoAPI.home_page,name = 'home_page'),
    path('admin/', admin.site.urls),
    path('api/', include('ipo_web.urls')),  # Include app-specific URLs
]

from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from ipo_web_app import settings
from .views import IPOInfoAPI

urlpatterns = [
    path('ipo_info/', IPOInfoAPI.as_view(), name='ipo_info'),
    path('', IPOInfoAPI.ipo_list_page, name='ipo_list_page'),  # Render IPO page
    path('data/', IPOInfoAPI.ipo_list_data, name='ipo_list_data'),
    path('admin-dashboard/', IPOInfoAPI.admin_dashboard, name='admin_dashboard'),
    path('ipo-list/', IPOInfoAPI.ipo_list_view, name='ipo_list'),
    # path('logout/', LogoutView.as_view(next_page='/admin/login/'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
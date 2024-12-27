from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import IPOInfoAPI

urlpatterns = [
    path('ipo_info/', IPOInfoAPI.as_view(), name='ipo_info'),
    path('', IPOInfoAPI.ipo_list_page, name='ipo_list_page'),  # Render IPO page
    path('data/', IPOInfoAPI.ipo_list_data, name='ipo_list_data'),
    path('admin-dashboard/', IPOInfoAPI.admin_dashboard, name='admin_dashboard'),
    # path('logout/', LogoutView.as_view(next_page='/admin/login/'), name='logout'),
]
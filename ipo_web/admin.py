from django.contrib import admin
from .models import IPOInfo

# Register the IPOInfo model
@admin.register(IPOInfo)
class IPOInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'ipo_date', 'price')  # Display fields in the admin table
    search_fields = ('company_name',)  # Search bar for filtering by company name

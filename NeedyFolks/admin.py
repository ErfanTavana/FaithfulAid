from django.contrib import admin
from .models import Needy

@admin.register(Needy)
class NeedyAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'national_code', 'phone_number', 'marital_status']
    search_fields = ['name', 'last_name', 'national_code', 'phone_number']
    list_filter = ['marital_status', 'gender']
    list_per_page = 20

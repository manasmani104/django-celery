# admin.py
from django.contrib import admin
from .models import Company, Department, Employee

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'department__name')
    list_filter = ('department',)

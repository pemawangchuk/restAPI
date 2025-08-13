from django.contrib import admin
from app.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department')
    search_fields = ('name', 'position', 'department')

admin.site.register(Employee, EmployeeAdmin)
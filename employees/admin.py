from django.contrib import admin

from .models import Employees, Color, Department
# Register your models here.

admin.site.register(Color)
admin.site.register(Department)
admin.site.register(Employees)
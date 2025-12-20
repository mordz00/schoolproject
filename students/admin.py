from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "age", "course", "created_at",)
    
admin.site.register(Student, StudentAdmin)
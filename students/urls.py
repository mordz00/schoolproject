from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='students'),
    path('students/details/<int:id>/', views.student_details, name='details'),
]

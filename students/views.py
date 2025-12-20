from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    return render(request, "home.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})

def student_details(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "details.html", {"student": student})

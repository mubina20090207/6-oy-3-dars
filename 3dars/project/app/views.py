from django.shortcuts import render
from .models import Course, Student

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def student_list(request):
    students = Student.objects.select_related('course').all()
    return render(request, 'student_list.html', {'students': students})

from django.urls import path
from .views import course_list, student_list

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('students/', student_list, name='student_list'),
]

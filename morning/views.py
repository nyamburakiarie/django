from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Teacher


# Create your views here.

# def home(request):
#     return HttpResponse("homepage")
#
#
# def about(request):
#     return HttpResponse("About us")
#
#
# def contact(request):
#     return HttpResponse("contact us")
#
#
# def services(request):
#   return HttpResponse("services")

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def location(request):
    return render(request, 'location.html')


def students(request):
    student = Student.objects.all()
    return render(request, 'students.html', {'student': student})


def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teacher': teachers})

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Welcome to the Homepage! This is a simple Django application.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is the About page of the Django application.")
    return render(request, 'about.html')
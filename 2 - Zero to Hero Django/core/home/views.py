from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   return render(request, 'home/index.html') # Pega o arquivo index.html na pasta templates e renderiza ele

def sucess_page(request):
    print("Sucess page accessed")
    return HttpResponse("<h1>Sucess Page!</h1> <h2>You have successfully created a Django server!</h2>")
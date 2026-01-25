from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        print(f"Recipe Name: {recipe_name}")
        print(f"Recipe Description: {recipe_description}")
        print(f"Recipe Image: {recipe_image}")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            image=recipe_image
        )
        return redirect('/recipes/')
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(recipe_name__icontains=search)

    context = {
        'recipes':queryset
    }
    return render(request, 'recipes.html', context) 

@login_required(login_url='/login/')
def delete_recipes(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.image = recipe_image
        queryset.save()
        return redirect('/recipes/')
    
    context = {
        'recipe':queryset
    }
    return render(request, 'update_recipes.html', context)

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password) # Criptografa a senha antes de salvar no banco de dados, importante para segurança. 
        user.save()
        messages.info(request, 'User created successfully!')

        return redirect('/register/')

    return render (request, 'register.html')
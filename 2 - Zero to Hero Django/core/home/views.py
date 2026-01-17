from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   peoples = [
       {'name': 'Abhijeet Gupta', 'age': 26},
       {'name': 'Bruno Reichert', 'age': 23},
       {'name': 'Charlie Johnson', 'age': 30},
       {'name': 'Diana Wood', 'age': 17},
       {'name': 'Ethan Nelson', 'age': 18},
       {'name': 'Fiona Cooke', 'age': 15},
       {'name': 'John Deer', 'age': 27},
       {'name': 'Jane Doe', 'age': 14},
   ]

   text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quaerat, deserunt asperiores nesciunt aspernatur dolores ea suscipit, qui nostrum, maxime dolor ad. Tenetur, magnam alias veritatis eos minus iure, ratione nisi voluptates omnis, non dolore facilis laboriosam. Doloremque cum soluta accusantium obcaecati autem beatae recusandae tenetur animi placeat dicta natus ipsum voluptate, laboriosam necessitatibus iure quos, ex velit reprehenderit non suscipit vel dolore et ea odit! Et, odio ex? Sed ipsam error odit ratione quisquam commodi aspernatur dolor, nisi illo doloremque, placeat similique? Ipsum, cupiditate nobis! Quos explicabo minus asperiores deserunt consequuntur alias ea dolore? Deserunt, commodi rem. Laudantium, modi impedit."

   vegetables = ['Pumpkin', 'Tomato', 'Potato', 'Cabbage', 'Broccoli']

   return render(request, 'home/index.html', context={'peoples': peoples, 'text': text, 'vegetables': vegetables, 'page': 'Home'}) # Pega o arquivo index.html na pasta templates e renderiza ele

def about(request):
    context = {'page': 'About'}
    return render(request, 'home/about.html', context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, 'home/contact.html', context)

def sucess_page(request):
    print("Sucess page accessed")
    return HttpResponse("<h1>Sucess Page!</h1> <h2>You have successfully created a Django server!</h2>")
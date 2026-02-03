from django.shortcuts import redirect, render
from django.http import HttpResponse
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings

# Create your views here.

def send_email(request):
    subject = "Greetings from Django App (plus file attachment!)"
    message = "This email is sent from a Django view function, and (if it's working properly) it should come with an attachment too!"
    recipient_list = ["brunowasborn2rock@gmail.com"]
    file_path = f"{settings.MEDIA_ROOT}/recipes/AR-82659-old-fashioned-onion-rings-DDMFS-beauty-3x4-0392e762554545be97798821fccb7e67.webp"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')

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
from home.models import *
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def run_this_function():
    print("Running this function from utils.py")
    time.sleep(2)
    print("Function execution completed!")

# Essa função deve ser executada dentro do shell do Django, não diretamente no navegador.

def send_email_to_client():
    subject = "Test Email from Django App"
    message = "This is a test email sent from the Django application."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["brunowasborn2rock@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)

def send_email_with_attachment(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
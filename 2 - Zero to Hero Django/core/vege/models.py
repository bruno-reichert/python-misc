from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # O Django tem um modelo de usuário embutido que pode ser usado para autenticação e gerenciamento de usuários.
    recipe_name = models.CharField(max_length=100, default='')
    recipe_description = models.TextField(default='')
    image = models.ImageField(upload_to='recipes/')


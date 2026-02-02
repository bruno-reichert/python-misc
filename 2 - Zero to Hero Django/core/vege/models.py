from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .utils import generate_slug

User = get_user_model()

# Create your models here.

class RecipesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # O Django tem um modelo de usuário embutido que pode ser usado para autenticação e gerenciamento de usuários.
    recipe_name = models.CharField(max_length=100, default='')
    slug = models.SlugField(unique=True, null=True, blank=True)
    recipe_description = models.TextField(default='')
    image = models.ImageField(upload_to='recipes/')
    recipe_view_count = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False) # Funciona como um soft delete, onde o registro não é realmente removido do banco de dados, mas marcado como excluído.

    objects = RecipesManager()
    admin_objects = models.Manager() # Permite acesso a todos os objetos, incluindo os marcados como excluídos.

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

class Department(models.Model):
    department = models.CharField(max_length=100)
    # date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False) # Funciona como um soft delete, onde o registro não é realmente removido do banco de dados, mas marcado como excluído.

    objects = StudentManager()
    admin_objects = models.Manager() # Permite acesso a todos os objetos, incluindo os marcados como excluídos.

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name='studentmarks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:
        unique_together = ['student', 'subject']

    def __str__(self) -> str:
        return f"{self.student.student_name} - {self.subject.subject_name}: {self.marks}"
    
class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name='studentreportcard', on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank', 'date_of_report_card_generation']
from django.contrib import admin
from tracker.models import Category, Transaction
from tracker.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Category)
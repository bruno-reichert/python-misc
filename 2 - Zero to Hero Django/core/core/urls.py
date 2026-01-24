"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'), # executa a a funcao home em views.py quando a raiz do site for acessada
    path('sucess/', sucess_page, name='sucess_page'),
    path('about/', about, name='about_page'),
    path('contact/', contact, name='contact_page'),
    path('admin/', admin.site.urls),

    path('recipes/', recipes, name='recipes'),
    path('delete_recipes/<int:id>/', delete_recipes, name='delete_recipes'),
    path('update_recipe/<int:id>/', update_recipe, name='update_recipe'),
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


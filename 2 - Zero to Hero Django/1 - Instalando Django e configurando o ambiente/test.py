import django
print(django.__version__)

'''
Para criar um projeto Django, utilize o comando:
django-admin startproject myproject

Ele criará uma estrutura de diretórios como esta:
myproject/
    manage.py - O script de gerenciamento do projeto
    myproject/
        __init__.py - Indica que este diretório é um pacote Python
        settings.py - Configurações do projeto
        urls.py - Definição das rotas do projeto
        wsgi.py - Configuração para servidores WSGI (Web Server Gateway Interface)
        asgi.py - Configuração para servidores ASGI (Asynchronous Server Gateway Interface)
'''
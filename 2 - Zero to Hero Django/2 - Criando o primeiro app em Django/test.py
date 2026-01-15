'''
Para criar um aplicativo Django, siga os seguintes passos:
1. Navegue até o diretório do seu projeto Django no terminal.
2. Execute o comando abaixo, substituindo "nome_do_app" pelo nome desejado para o seu aplicativo:

   python manage.py startapp nome_do_app

Com isso, um novo diretório chamado "nome_do_app" será criado dentro do seu projeto, contendo a estrutura básica de arquivos para o aplicativo Django, incluindo models.py, views.py, admin.py, entre outros.
'''

'''
Apps Django são componentes modulares que encapsulam funcionalidades específicas dentro de um projeto Django. Eles permitem organizar o código de forma mais eficiente, facilitando a manutenção e a reutilização. Cada app pode conter modelos de dados, visualizações, URLs, templates e arquivos estáticos relacionados a uma funcionalidade específica do projeto. Por exemplo, em um site de comércio eletrônico, você pode ter apps separados para gerenciamento de produtos, carrinho de compras e processamento de pagamentos. Como apps, desenvolvedores podem trabalhar em diferentes partes do projeto de forma independente, promovendo uma arquitetura mais limpa e escalável, e possibilitando a reutilização de apps em múltiplos projetos Django (por exemplo, um app de autenticação pode ser reutilizado em vários sites).
'''

'''
Para iniciar o servidor de desenvolvimento do Django, você deve usar o comando abaixo no terminal, estando no diretório raiz do seu projeto Django:
    python manage.py runserver

Isso te permitirá acessar o servidor localmente através do navegador, geralmente no endereço http://127.0.0.1:8000/ ou http://localhost:8000/. Além disso, é possível especificar uma porta diferente adicionando-a ao comando, por exemplo:
    python manage.py runserver 0.0.0.0:5000
'''

'''
Toda vez que um app Django é criado, é necessário registrá-lo no arquivo settings.py do projeto para que o Django reconheça e inclua o app na configuração do projeto. Isso é feito adicionando o nome do app à lista INSTALLED_APPS dentro do arquivo settings.py. Por exemplo, se você criou um app chamado "blog", você deve adicionar 'blog', à lista INSTALLED_APPS, como mostrado abaixo:
INSTALLED_APPS = [ [...], 'blog', [...] ]

Além disso, é possível criar uma lista separada para apps externos ou personalizados e depois concatená-la à lista INSTALLED_APPS, facilitando a organização e manutenção das configurações do projeto.
'''
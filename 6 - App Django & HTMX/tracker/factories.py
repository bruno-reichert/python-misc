import factory
from factory.faker import Faker
from factory.declarations import Iterator, Sequence
from factory import SubFactory # type: ignore
from tracker.models import User, Category, Transaction
from datetime import datetime

'''
Classes FactoryBoy são utilizadas para criar instâncias de modelos de forma simplificada e consistente para testes. Elas permitem gerar dados de teste de maneira fácil e rápida, evitando a necessidade de criar manualmente objetos para cada teste. As classes FactoryBoy são definidas como subclasses de factory.django.DjangoModelFactory e especificam o modelo que estão criando, bem como os campos e seus valores.
'''

class UserFactory(factory.django.DjangoModelFactory):
    class Meta: # type: ignore
        model = User # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    username = Sequence(lambda n: 'user%d' % n)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta: # type: ignore
        model = Category
        django_get_or_create = ('name',)

    name = Iterator(['Bills', 'Housing', 'Salary', 'Food', 'Social'])

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta: # type: ignore
        model = Transaction

    user = SubFactory(UserFactory)
    category = SubFactory(CategoryFactory)
    amount = 5
    date = Faker('date_between',
    start_date = datetime(year=2022, month=1, day=1).date(),
    end_date = datetime.now().date()
    )
    type = Iterator(
        [
            x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES
        ]
    )
    type = Iterator(['income', 'expense'])

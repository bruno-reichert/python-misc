import pytest
from tracker.factories import TransactionFactory, UserFactory

@pytest.fixture # Uma fixture pytest é uma função que pode ser usada para fornecer dados ou objetos de teste para os testes. Ela é decorada com @pytest.fixture e pode ser usada em qualquer função de teste que precise desses dados ou objetos.
def transactions():
    return TransactionFactory.create_batch(20)

# Qualquer fixture criada em um arquivo conftest.py estará disponível para todos os testes na mesma pasta e em subpastas. Isso significa que a fixture transactions pode ser usada em qualquer teste dentro da pasta tracker/tests ou em subpastas, sem a necessidade de importá-la explicitamente.

@pytest.fixture
def user_transactions():
    user = UserFactory()
    return TransactionFactory.create_batch(20, user=user)

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def transaction_dict_params(user):
    transaction = TransactionFactory(user=user)
    return {
        'type': transaction.type,
        'amount': transaction.amount,
        'date': transaction.date,
        'category': transaction.category_id,
    }
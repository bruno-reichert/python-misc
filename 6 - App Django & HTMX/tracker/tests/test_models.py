import pytest
from tracker.models import Transaction

@pytest.mark.django_db
def test_queryset_get_income_method(transactions):
    # O método get_income deve retornar apenas as transações do tipo 'income'
    qs = Transaction.objects.get_income() # type: ignore
    if qs.count() > 0:
        assert all(t.type == 'income' for t in qs)

@pytest.mark.django_db
def test_queryset_get_expenses_method(transactions):
    # O método get_income deve retornar apenas as transações do tipo 'expense'
    qs = Transaction.objects.get_expenses() # type: ignore
    if qs.count() > 0:
        assert all(t.type == 'expense' for t in qs)


@pytest.mark.django_db
def test_queryset_get_total_income_method(transactions):
    total_income = Transaction.objects.get_total_income() # type: ignore
    assert total_income == sum(t.amount for t in transactions if t.type == 'income')

@pytest.mark.django_db
def test_queryset_get_total_expenses_method(transactions):
    total_expenses = Transaction.objects.get_total_expenses() # type: ignore
    assert total_expenses == sum(t.amount for t in transactions if t.type == 'expense')
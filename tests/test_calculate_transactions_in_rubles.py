import pytest

from src.utils import calculate_transactions_in_rubles


@pytest.fixture
def rubles_transaction():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


# Создаем фикстуру для транзакции в долларах
@pytest.fixture
def dollars_transaction():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_calculate_transactions_in_rubles_valid(rubles_transaction):
    result = calculate_transactions_in_rubles(rubles_transaction)
    assert isinstance(result, float)
    assert result == 31957.58


def test_calculate_transactions_in_rubles_invalid_currency(dollars_transaction):
    with pytest.raises(ValueError, match="Транзакция выполнена не в рублях. Укажите транзакцию в рублях"):
        calculate_transactions_in_rubles(dollars_transaction)
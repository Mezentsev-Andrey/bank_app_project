import pytest

from src.generators import transaction_descriptions, transactions


@pytest.fixture
def input_transactions() -> list[dict]:
    """
    Фикстура для предоставления входных транзакций
    :return: cписок входных транзакций доступных для использования
    """
    return transactions


# Тестовая функция, использующая фикстуру
def test_transaction_descriptions(input_transactions: list[dict]) -> None:
    """
    Тестовая функция, проверяющая функцию формирования описаний транзакций
    :param input_transactions:входные транзакции, используемые для тестирования
    :return: None
    """
    result = list(transaction_descriptions(input_transactions))

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected_descriptions

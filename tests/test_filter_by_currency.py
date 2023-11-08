import pytest

from src.generators import filter_by_currency, transactions


@pytest.fixture
def input_transactions() -> list[dict]:
    """
    Фикстура для предоставления входных транзакций
    :return: переменная содержащая входные транзакции
    """
    return transactions


def test_filter_by_currency(input_transactions: list[dict]) -> None:
    """
    Тестовая функция, проверяющая правильность фильтрации транзакций по валюте "USD"
    :param input_transactions: входной список транзакций
    :return: None
    """
    filtered_transactions = list(filter_by_currency(input_transactions, "USD"))
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in filtered_transactions)


def test_filter_by_currency_with_valid_currency(input_transactions: list[dict]) -> None:
    """
    Тестовая функция, проверяющая получение трех операций с валютой USD
    :param input_transactions: входной список транзакций
    :return: None
    """
    result = list(filter_by_currency(input_transactions, "USD"))
    assert len(result) == 3  #
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in result)


def test_filter_by_currency_with_invalid_currency(input_transactions: list[dict]) -> None:
    """
    Тестовая функция, проверяеющая отсутствие транзакций с валютой EUR
    :param input_transactions: входной список транзакций
    :return: None
    """
    result = list(filter_by_currency(input_transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_with_empty_transactions() -> None:
    """
    Тестовая функция, проверяющая отсутствие транзакций в пустом списке
    :return: None
    """
    filtered_transactions = list(filter_by_currency([], "USD"))
    assert len(filtered_transactions) == 0


def test_filter_by_currency_with_rub(input_transactions: list[dict]) -> None:
    """
    Тестовая функция, проверяющая правильность фильтрации транзакций по валюте "RUB"
    :param input_transactions: входной список транзакций
    :return: None
    """
    result = list(filter_by_currency(input_transactions, "RUB"))
    assert len(result) == 2
    assert all(transaction["operationAmount"]["currency"]["code"] == "RUB" for transaction in result)

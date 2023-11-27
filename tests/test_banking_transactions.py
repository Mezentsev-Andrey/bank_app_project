import pytest

from src.banking_transactions import searching_data_by_string, searching_dictionaries_by_category


# Фикстура с тестовыми данными
@pytest.fixture
def list_of_transactions() -> list[dict]:
    """
    Фикстура, которая возвращает список словарей, представляющих собой банковские транзакции.
    :return: список словарей с данными о банковских транзакциях.
    """
    return [
        {
            "id": "650703",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency name": "Sol",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency name": "Peso",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5380041",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789,
            "currency name": "Peso",
            "description": "Открытие вклада",
        },
    ]


@pytest.fixture
def search_string() -> str:
    """
    Фикстура для строки поиска.
    :return: возвращает строку для использования в тестах.
    """
    return "Перевод организации"


def test_searching_data_by_string(list_of_transactions: list[dict], search_string: str) -> None:
    """
    Тестовая функция выполняющая поиск данных в списке транзакций по заданной строке.
    :param list_of_transactions:список словарей с данными о банковских транзакциях.
    :param search_string: строка для поиска
    :return: None
    """
    result_list = searching_data_by_string(list_of_transactions, search_string)
    expected_result = [
        {
            "id": "650703",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency name": "Sol",
            "description": "Перевод организации",
        }
    ]

    assert result_list == expected_result


@pytest.fixture
def list_dictionaries() -> list[dict]:
    """
    Фикстура, возвращающая тестовые данные в виде списка словарей.
    :return: тестовый список словарей
    """
    return [
        {
            "id": "650703",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency name": "Sol",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency name": "Peso",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "5380041",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789,
            "currency name": "Peso",
            "description": "Открытие вклада",
        },
    ]


@pytest.fixture
def category_dictionary() -> dict:
    """
    Фикстура, возвращающая тестовые данные в виде словаря с категориями.
    :return: словарь с категориями.
    """
    return {"1": "Перевод организации", "2": "Перевод с карты на карту", "3": "Открытие вклада"}


def test_searching_dictionaries_by_category(list_dictionaries: list[dict], category_dictionary: dict) -> None:
    """
    Тестовая функция выполняющая поиск данных в списке словарей по категориям,
    используя словарь с категориями.
    :param list_dictionaries: список словарей.
    :param category_dictionary: список с категориями.
    :return: None.
    """
    result_dictionary = searching_dictionaries_by_category(list_dictionaries, category_dictionary)
    expected_result = {"Перевод организации": 1, "Перевод с карты на карту": 1, "Открытие вклада": 1}
    assert result_dictionary == expected_result

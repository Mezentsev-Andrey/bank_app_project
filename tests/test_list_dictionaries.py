import pytest

from src.processing import filter_by_state, sort_dict_list


@pytest.fixture
def collection_dictionaries_list() -> list[dict]:
    """
    Фикстура создающая и возвращающая список словарей, представляющих собой коллекцию данных о транзакциях
    :return: список словарей, представляющих коллекцию данных о транзакциях
    """
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(collection_dictionaries_list: list[dict]) -> None:
    """
    Тестовая функция принимающая список словарей и фильтруеющая его, оставляя только те элементы,
    у которых значение ключа 'state' соответствует заданному состоянию
    :param collection_dictionaries_list: cписок словарей, представляющих коллекцию данных о транзакциях
    :return: None
    """
    assert filter_by_state(collection_dictionaries_list, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_dict_list(collection_dictionaries_list: list[dict]) -> None:
    """
    Тестовая функция принимающая список словарей и сортирующая их по ключу 'date' в заданном порядке
    :param collection_dictionaries_list: cписок словарей, представляющих коллекцию данных о транзакциях
    :return: None
    """
    assert sort_dict_list(collection_dictionaries_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

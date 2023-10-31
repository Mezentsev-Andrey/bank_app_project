from datetime import datetime


input_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей фильтрует входные данные и возвращает новый список,
    содержащий словари только с указанным значением ключа state.
    :param data: параметр принимающий на вход список словарей.
    :param state:опциональный параметр с значением по умолчанию 'EXECUTED'.
    :return:новый список, содержащий словари только с указанным значением ключа state.
    """
    filtered_data = [item for item in data if item.get("state") == state]
    return filtered_data


# Вызов функции с значением state 'EXECUTED'
output_default = filter_by_state(input_data, state="EXECUTED")
print("Если передано 'EXECUTED':", output_default)

# Вызов функции с значением state 'CANCELED'
output_canceled = filter_by_state(input_data, state="CANCELED")
print("Если передано 'CANCELED':", output_canceled)


def sort_dict_list(dict_list: list[dict], reverse_order: bool = True) -> list[dict]:
    """
    Функция, сортирует список словарей по убыванию или возрастанию даты.
    :param dict_list: список словарей для сортировки.
    :param reverse_order: параметр указывающий порядок сортировки (по умолчанию True - убывание).
    :return: отсортированный список словарей.
    """
    # Преобразование строки с датой в объект datetime и сортировка списка по дате
    sorted_list = sorted(
        dict_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse_order
    )
    return sorted_list


# Проверка работспособности функции.
sorted_list = sort_dict_list(input_data, reverse_order=True)
print("Сортировка списка по убыванию:", sorted_list)

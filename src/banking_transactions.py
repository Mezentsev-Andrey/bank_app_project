import re

import pandas as pd


def searching_data_by_string(list_dictionaries: list[dict], string: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска, возвращая список словарей,
    у которых в описании есть данная строка.
    :param list_dictionaries: список словарей
    :param string: строка по которой идет поиск
    :return: список словарей
    """
    df = pd.DataFrame(list_dictionaries)
    pattern = re.compile(string, re.IGNORECASE)
    result_df = df[df["description"].apply(lambda x: bool(re.search(pattern, x)))]
    result = result_df.to_dict(orient="records")
    return result


def searching_dictionaries_by_category(list_dictionaries: list[dict], category_dictionary: dict) -> dict:
    """
    Функция которая принимает список словарей с данными о банковских операциях и категорий операций.
    :param list_dictionaries: список словарей с данными о банковских операциях и категорий операций.
    :param category_dictionary: словарь с категориями.
    :return: словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории.
    """
    operation_count = {category_name: 0 for category_name in category_dictionary.values()}
    for transaction in list_dictionaries:
        category_code = transaction.get("description")
        if category_code in operation_count:
            operation_count[category_code] += 1
    return operation_count

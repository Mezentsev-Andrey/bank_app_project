import json


def read_transactions_from_file(file_path):
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    :param file_path: путь к списку словарей финансовых транзакций из json файла.
    :return: список словарей с данными  из json файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            print(f"Файл {file_path} не содержит список транзакций.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON файла {file_path}.")
    return []


def calculate_transactions_in_rubles(transaction):
    """
    Функция, которая принимает на вход одну транзакцию.
    :param transaction: входная одна транзакция.
    :return:сумму транзакции (amount) в рублях, возвращает тип float, если транзакция совершалась в рублях,
    возвращает ошибку ValueError если транзакция была совершена в другой валюте.
    """
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    if currency_code == "RUB":
        return amount
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")

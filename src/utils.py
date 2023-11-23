import json
import logging
from typing import Any

# Создаем логгер
logger = logging.getLogger(__name__)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler("utils.log", mode="w", encoding="utf-8")

# Создаем форматтер для определения формата записи лога
formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def read_transactions_from_file(file_path: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях.
    :param file_path: путь к списку словарей финансовых транзакций из json файла.
    :return: список словарей с данными  из json файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            logger.info("Функция отработала без ошибок.")
            return data
        else:
            logger.error(f"Файл {file_path} не содержит список транзакций.")
    except FileNotFoundError:
        logger.warning(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        logger.error(f"Ошибка чтения JSON файла {file_path}.")
    return []


# Проверка работоспособности логгера
# transaction = read_transactions_from_file(JSON_PATH)


def calculate_transactions_in_rubles(transaction: Any) -> Any:
    """
    Функция, которая принимает на вход одну транзакцию.
    :param transaction: одна входная  транзакция.
    :return: сумму транзакции (amount) в рублях, возвращает тип float, если транзакция совершалась в рублях,
    возвращает ошибку ValueError если транзакция была совершена в другой валюте.
    """

    try:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])

        if currency_code == "RUB":
            logger.info("Транзакция выполнена в рублях успешно.")
            return amount
        else:
            # Запись предупреждения о неверной валюте в лог
            logger.warning("Транзакция выполнена не в рублях. Укажите транзакцию в рублях.")
    except Exception as error:
        # Запись других неожиданных ошибок в лог
        logger.error(f"Неожиданная ошибка {error} при расчете транзакций в рублях.")
        raise
        return "Неожиданная ошибка {error} при расчете транзакций в рублях."


# Проверка вывода логгирования и работы функции
transaction_data = {"operationAmount": {"amount": "100.50", "currency": {"code": "USD"}}}
calculate_transactions_in_rubles(transaction_data)

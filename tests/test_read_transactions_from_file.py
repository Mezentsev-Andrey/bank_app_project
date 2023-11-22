import json
from typing import Any

import pytest

from src.utils import read_transactions_from_file


@pytest.fixture
def valid_json_file(tmp_path: Any) -> str:
    """
    Фикстура для создания временного JSON-файла с корректными тестовыми данными.
    :param tmp_path: путь до временной директории.
    :return: возвращает путь к созданному временному файлу.
    """
    test_data = [
        {"id": 441945886, "amount": 31957.58, "currency": "RUB", "description": "Перевод организации"},
        {"id": 41428829, "amount": 8221.37, "currency": "USD", "description": "Перевод организации"},
    ]
    file_path = "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_data, file)
    return file_path


def test_read_transactions_from_file_valid_json(valid_json_file: str) -> None:
    """
    Тестовая функция проверки корректного чтения транзакций из JSON-файла.
    :param valid_json_file: путь к JSON-файлу с корректными данными транзакций.
    :return: ничего не возвращает.
    """
    transactions = read_transactions_from_file(valid_json_file)
    assert isinstance(transactions, list)
    assert len(transactions) == 2
    assert transactions[0]["id"] == 441945886
    assert transactions[1]["description"] == "Перевод организации"


def test_read_transactions_from_file_empty_file(valid_json_file: str) -> None:
    """
    Тестовая функция для проверки корректной обработку пустого JSON-файла.
    :param valid_json_file: путь к JSON-файлу с корректными данными транзакций.
    :return: проверяет, что результат функции при чтении пустого файла равен пустому списку.
    """
    empty_file_path = "empty_data.json"
    with open(empty_file_path, "w", encoding="utf-8") as file:
        file.write("")
    transactions = read_transactions_from_file(empty_file_path)
    assert transactions == []


def test_read_transactions_from_file_nonexistent_file(valid_json_file: str) -> None:
    """
    Тестовая функция проверяющая корректную обработку отсутствующего JSON-файла.
    :param valid_json_file: путь к JSON-файлу с корректными данными транзакций.
    :return: проверяет, что результат функции при чтении несуществующего файла равен пустому списку.
    """
    non_existent_file_path = "non_existent.json"
    with open(non_existent_file_path, "w", encoding="utf-8") as file:
        file.write("non existent json file")
    transactions = read_transactions_from_file(non_existent_file_path)
    assert transactions == []


def test_read_transactions_from_file_invalid_json(valid_json_file: str) -> None:
    """
    Тестовая функция проверяющая корректную обработку недопустимого JSON-файла.

    :param valid_json_file: путь к JSON-файлу с корректными данными транзакций.
    :return: проверяет, что результат функции при чтении файла с некорректными данными равен пустому списку.
    """
    invalid_file_path = "invalid_data.json"
    with open(invalid_file_path, "w", encoding="utf-8") as file:
        file.write("invalid json data")
    transactions = read_transactions_from_file(invalid_file_path)
    assert transactions == []

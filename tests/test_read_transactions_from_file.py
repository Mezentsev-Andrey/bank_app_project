import json

import pytest

from src.utils import read_transactions_from_file


@pytest.fixture
def valid_json_file(tmp_path):
    test_data = [
        {"id": 441945886, "amount": 31957.58, "currency": "RUB", "description": "Перевод организации"},
        {"id": 41428829, "amount": 8221.37, "currency": "USD", "description": "Перевод организации"},
    ]
    file_path = "test_data.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(test_data, file)
    return file_path


def test_read_transactions_from_file_valid_json(valid_json_file):
    transactions = read_transactions_from_file(valid_json_file)
    assert isinstance(transactions, list)
    assert len(transactions) == 2
    assert transactions[0]["id"] == 441945886
    assert transactions[1]["description"] == "Перевод организации"


def test_read_transactions_from_file_empty_file(valid_json_file):
    empty_file_path = "empty_data.json"
    with open(empty_file_path, "w", encoding="utf-8") as file:
        file.write("")
    transactions = read_transactions_from_file(empty_file_path)
    assert transactions == []


def test_read_transactions_from_file_nonexistent_file(valid_json_file):
    non_existent_file = "non_existent.json"
    transactions = read_transactions_from_file(non_existent_file)
    assert transactions == []


def test_read_transactions_from_file_invalid_json(tmp_path):
    invalid_file_path = "invalid_data.json"
    with open(invalid_file_path, "w", encoding="utf-8") as file:
        file.write("invalid json data")
    transactions = read_transactions_from_file(invalid_file_path)
    assert transactions == []

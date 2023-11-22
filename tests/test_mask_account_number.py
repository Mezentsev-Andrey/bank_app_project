import pytest

from src.masks import mask_account_number


@pytest.mark.parametrize(
    "account_number, expected_output, expected_log",
    [
        ("34567892145689487654", "**7654", "Успешное маскирование номера счета: **7654"),
        ("123456789890", "Неверно введен номер счета", "Неверно введен номер счета"),
        ("", "Неверно введен номер счета", "Неверно введен номер счета"),
    ],
)
def test_mask_account_number(account_number: str, expected_output: str, expected_log: str) -> None:
    """
    Тестовая функция проверяющая функцию маскирования номера счета
    :param account_number: номер счета для маскирования
    :param expected_output: ожидаемый результат после маскирования
    :return: None
    """
    result = mask_account_number(account_number)
    assert result == expected_output
    if expected_output is None:
        assert "Неверно введен номер счета" in expected_log
    else:
        assert f"{expected_output}" in expected_log

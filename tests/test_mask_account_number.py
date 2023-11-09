import pytest

from src.masks import mask_account_number


@pytest.mark.parametrize("account_number, expected", [("234567890345671", "**5671"), ("", "**")])
def test_mask_account_number(account_number: str, expected: str) -> None:
    """
    Тестовая функция проверяющая функцию маскирования номера счета
    :param account_number: номер счета для маскирования
    :param expected: ожидаемый результат после маскирования
    :return: None
    """
    assert mask_account_number(account_number) == expected

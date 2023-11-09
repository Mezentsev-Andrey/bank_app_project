import pytest

from src.masks import mask_card_number


@pytest.mark.parametrize("card_number, expected", [("1234567890234567", "1234 56** **** 4567"), ("", " ** **** ")])
def test_mask_card_number(card_number: str, expected: str) -> None:
    """
    Тестовая функция проверяющая функцию маскирования номера счета
    :param card_number: номер счета для маскирования
    :param expected: ожидаемый результат после маскирования
    :return: None
    """
    assert mask_card_number(card_number) == expected

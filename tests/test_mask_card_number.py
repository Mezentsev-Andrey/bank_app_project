import pytest

from src.masks import mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_output, expected_log",
    [
        ("1234567890233457", "1234 56** **** 3457", "Успешное маскирование номера карты: 1234 56** **** 3457"),
        ("456789021345", "Неверно введен номер карты", "Неверно введен номер карты"),
        ("", "Неверно введен номер карты", "Неверно введен номер карты"),
    ],
)
def test_mask_card_number(card_number: str, expected_output: str, expected_log: str) -> None:
    """
    Тестовая функция проверяющая функцию маскирования номера счета.
    :param card_number: номер счета для маскирования.
    :param expected_output: ожидаемый результат после маскирования.
    :return: None
    """
    result = mask_card_number(card_number)
    assert result == expected_output
    if expected_output is None:
        assert "Неверно введен номер карты" in expected_log
    else:
        assert f"{expected_output}" in expected_log

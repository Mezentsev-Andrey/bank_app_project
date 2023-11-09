import pytest

from src.widget import get_card_or_account_info


@pytest.mark.parametrize(
    "numeric_object, expected",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Mastercard 7158300734726758", "Mastercard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_get_card_or_account_info(numeric_object: str, expected: str) -> None:
    """
    Тестовая функция принимающая строку, содержащую информацию о карте или счете,
    и заменяющая символы в номере, кроме первых и последних,на символы "*"
    :param numeric_object: параметр содержащий информацию о карте или счете
    :param expected: ожидаемый результат после обработки
    :return: None
    """
    assert get_card_or_account_info(numeric_object) == expected

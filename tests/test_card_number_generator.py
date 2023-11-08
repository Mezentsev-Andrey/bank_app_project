from typing import Generator

import pytest

from src.generators import card_number_generator


@pytest.fixture
def card_number_generator_instance() -> Generator:
    """
    Фикстура для создания экземпляра генератора номеров карт
    :return: экземпляр генератора номеров карт
    """
    start = 1000
    end = 1010
    return card_number_generator(start, end)


def test_card_number_generator(card_number_generator_instance: str) -> None:
    """
    Тестовая функция, проверяющая соответствует ли генератор номеров карт заданным критериям
    :param card_number_generator_instance:парметр содержащий сгенерированные номера карт
    :return: None
    """
    generated_card_numbers = list(card_number_generator_instance)
    assert len(generated_card_numbers) == 11
    assert generated_card_numbers[0] == "0000 0000 0000 1000"
    assert generated_card_numbers[-1] == "0000 0000 0000 1010"


def test_card_number_format(card_number_generator_instance: str) -> None:
    """
    Тестовая функция, проверяющая формат сгенерированных номеров карт
    :param card_number_generator_instance:параметр содержащий сгенерированные номера карт
    :return: None
    """
    generated_card_numbers = list(card_number_generator_instance)
    for card_number in generated_card_numbers:
        assert len(card_number) == 19
        assert card_number[:4].isdigit()
        assert card_number[5:9].isdigit()
        assert card_number[10:14].isdigit()
        assert card_number[15:].isdigit()
        assert card_number[4] == " " and card_number[9] == " " and card_number[14] == " "

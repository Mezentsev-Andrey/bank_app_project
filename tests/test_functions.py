import pytest

from src.masks import mask_account_number, mask_card_number
from src.processing import filter_by_state, sort_dict_list
from src.widget import convert_date_format, get_card_or_account_info


@pytest.fixture
def card_number(card_number: str) -> str:
    card_number = str(card_number)
    return card_number


@pytest.mark.parametrize("card_number, expected", [("1234567890234567", "1234 56** **** 4567"), ("", " ** **** ")])
def test_mask_card_number(card_number: str, expected) -> None:
    assert mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [("234567890345671", "**5671"), ("", "**")])
def test_mask_account_number(account_number: str, expected) -> None:
    assert mask_account_number(account_number) == expected


@pytest.mark.parametrize(
    "numeric_object, expected",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Mastercard 7158300734726758", "Mastercard 7158 30** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_get_card_or_account_info(numeric_object: str, expected) -> None:
    assert get_card_or_account_info(numeric_object) == expected


def test_convert_date_format() -> None:
    assert convert_date_format("2019-07-11T02:26:18.671407") == "11.07.2019"


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state(data: list[dict], expected, state: str = "EXECUTED") -> None:
    assert filter_by_state(data, state) == expected


@pytest.mark.parametrize(
    "dict_list, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort_dict_list(dict_list: list[dict], expected, reverse_order: bool = True) -> None:
    assert sort_dict_list(dict_list, reverse_order) == expected

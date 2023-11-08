from src.widget import convert_date_format


def test_convert_date_format() -> None:
    """
    Тестовая функция проверяющая правильность конвертируемости формата даты.
    :return: None
    """
    assert convert_date_format("2019-07-11T02:26:18.671407") == "11.07.2019"

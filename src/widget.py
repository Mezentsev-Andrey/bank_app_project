from masks import mask_card_number, mask_account_number


def get_card_or_account_info(numeric_object: str) -> str:
    """
    Функция принимает на вход строку с информацией тип карты/счета и номер карты/счета.
    :param numeric_object: входные данные типа/счета и номера карты/счета.
    :return: возвращает строку с замаскированным номером карты/счета.
    """
    numeric_object_list = numeric_object.split()
    if "Счет" in numeric_object:
        return f"{numeric_object_list[0].title()} {mask_account_number(numeric_object_list[1])}"
    elif numeric_object_list[1].isalpha():
        return (
            f"{numeric_object_list[0].title()} {numeric_object_list[1].title()} "
            f"{mask_card_number(numeric_object_list[2])}"
        )
    else:
        return f"{numeric_object_list[0].title()} {mask_card_number(numeric_object_list[1])}"


# проверка работоспособности функции
numeric_object = "Visa Platinum 8990922113665229"
result = get_card_or_account_info(numeric_object)
print(result)


def convert_date_format(input_date: str) -> str:
    """
    функция, которая принимает на вход строку, вида "2018-07-11T02:26:18.671407
    :param input_date: входящая информация о дате
    :return: возвращает строку с датой в виде "11.07.2018"
    """
    date_parts = input_date.split("-")
    # Извлекаем день, месяц и год
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2][:2]
    # Формируем новую строку с датой в формате "дд.мм.гггг"
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date


# проверка работоспособности функции
input_date = "2019-07-11T02:26:18.671407"
result = convert_date_format(input_date)
print(result)

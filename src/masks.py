def mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    :param card_number: входящий номер карты.
    :return:возвращает замаскированный номер карты.
    """
    mask_card = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card


def mask_account_number(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску.
    :param account_number:входящий номер счета.
    :return:возвращает замаскированный номер счета
    """
    mask_account = "**" + account_number[-4:]
    return mask_account

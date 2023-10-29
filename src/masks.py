def mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    :param card_number:
    :return:
    """
    mask_card = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
    return mask_card


card_number = "1234567890234567"
masked_card_number = mask_card_number(card_number)
print(masked_card_number)


def mask_account_number(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску.
    :param account_number:
    :return:
    """
    mask_account = '**' + account_number[-4:]
    return mask_account


account_number = "234567890345671"
masked_account_number = mask_account_number(account_number)
print(masked_account_number)

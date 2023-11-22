import logging

# Создаем логгер
logger = logging.getLogger(__name__)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler("masks.log", mode="w", encoding="utf-8")

# Создаем форматтер для определения формата записи лога
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    :param card_number: входящий номер карты.
    :return:возвращает замаскированный номер карты.
    """
    if len(card_number) == 16:
        mask_card = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info(f"Успешное маскирование номера карты: {mask_card}")
        return mask_card
    else:
        logger.error("Неверно введен номер карты")
        return "Неверно введен номер карты"


# Проверка вывода логгирования и работы функции
mask_card_number("1234567890233457")
mask_card_number("456789021345")
mask_card_number("")


def mask_account_number(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску.
    :param account_number: входящий номер счета.
    :return: возвращает замаскированный номер счета
    """
    if len(account_number) == 20:
        mask_account = "**" + account_number[-4:]
        logger.info(f"Успешное маскирование номера счета: {mask_account}")
        return mask_account
    else:
        logger.error("Неверно введен номер счета")
        return "Неверно введен номер счета"


# Проверка вывода логгирования и работы функции
mask_account_number("34567892145689487654")
mask_account_number("123456789890")
mask_account_number("")

import os
from datetime import datetime
from typing import Any

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "arg_1, arg_2, expected_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}")]
)
def test_log_decorator(arg_1: int, arg_2: int, expected_result: str) -> None:
    """
    Тестовая функия проверяет поведение функции log_decorator при конкретных входных данных.
    :param arg_1: первый аргумент для функции, которую тестируем.
    :param arg_2: второй аргумент для функции, которую тестируем.
    :param expected_result:
    :return: ожидаемый результат или сообщение об ошибке для заданных входных данных.
    """
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def foo(x: int, y: int) -> float:
        """
        Функция используется для демонстрации декоратора log().
        :param x: первый аргумент функции.
        :param y: второй аргумент функции.
        :return: результат выполнения функции.
        """
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    with open(filename) as file:
        log_message = file.read().strip()

        expected_log = now + expected_result

        assert log_message == expected_log


@pytest.mark.parametrize(
    "arg_1, arg_2, expected_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}")]
)
def test_console_log(capsys: Any, arg_1: int, arg_2: int, expected_result: str) -> None:
    """
    Тестовая функция для проверки вывода логов в консоль при использовании декоратора log().
    :param capsys: встроенный объект pytest для захвата вывода в консоль.
    :param arg_1: первый аргумент для функции, которую тестируем.
    :param arg_2: второй аргумент для функции, которую тестируем.
    :param expected_result: ожидаемый результат или сообщение в логах для заданных входных данных.
    :return: Npne
    """

    @log()
    def foo(x: int, y: int) -> float:
        """
        Функция используется для демонстрации декоратора log().
        :param x: первый аргумент функции.
        :param y: второй аргумент функции.
        :return: результат выполнения функции.
        """
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    expected_log = now + expected_result

    log_message = capsys.readouterr()

    assert log_message.out.strip() == expected_log

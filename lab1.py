# -*- coding: utf-8 -*-
"""
Практична робота №1
Дисципліна: «Об'єктно-орієнтоване проєктування СУ»
Тема: «Математичні обчислення у Python»
Варіант: Integer2, Табл.2 (варіант 2), Boolean3

Запуск:
    python lab1.py
"""

import math
from math import exp, sqrt, tan, sin, radians, log


def cbrt(value: float) -> float:
    """Кубічний корінь ³√value для дійсних чисел (коректно і для від’ємних)."""
    return math.copysign(abs(value) ** (1.0 / 3.0), value)


def task_integer2() -> None:
    """
    Integer2.
    Дана маса M (кг). Знайти кількість повних тонн у ній (1 т = 1000 кг),
    використовуючи цілочисельне ділення.
    """
    try:
        m = int(input("M (kg) = ").strip())
        if m < 0:
            raise ValueError("M must be >= 0")
    except ValueError:
        print("Input error! M must be a non-negative INTEGER.")
        return

    tons = m // 1000
    print("Full tons =", tons)


def task_real2() -> None:
    """
    Табл.2, варіант 2.
    Обчислити:

        y = [ e^(x+0.5) * sqrt(|x - tg(x+13°) + 25|) ] / [ ³√( sin^2(x^3) * log_5(|x|) ) ]

    Примітки:
    - tan/sin працюють у радіанах, тому 13° переводимо через radians(13).
    - log(|x|, 5) визначений тільки для x != 0.
    """
    try:
        x = float(input("Enter x = ").strip())
    except ValueError:
        print("Input error! x must be a NUMBER.")
        return

    a = radians(13.0)

    try:
        if x == 0:
            raise ValueError("x must be non-zero because log5(|x|) is undefined for x=0")

        log5_absx = log(abs(x), 5)

        sin_part = (sin(x ** 3)) ** 2
        inside = sin_part * log5_absx

        # Якщо inside == 0, то ³√inside == 0 і буде ділення на нуль.
        if inside == 0:
            raise ZeroDivisionError("Denominator becomes zero (inside cbrt is 0)")

        numerator = exp(x + 0.5) * sqrt(abs(x - tan(x + a) + 25))
        denominator = cbrt(inside)

        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero")

        y = numerator / denominator
    except Exception:
        print("Calculation error! Check input and domain restrictions.")
        return

    print("y =", y)


def task_boolean3() -> None:
    """
    Boolean3.
    Дано ціле число A. Перевірити істинність висловлювання:
    «Число A є парним».
    """
    try:
        a = int(input("A = ").strip())
    except ValueError:
        print("Input error! A must be an INTEGER.")
        return

    res = (a % 2 == 0)
    print("A is even:", res)


def main_menu() -> None:
    """Просте меню запуску завдань."""
    while True:
        print("\n=== Практична робота №1 ===")
        print("1) Integer2 (повні тонни)")
        print("2) Табл.2 (вираз, варіант 2)")
        print("3) Boolean3 (парність A)")
        print("0) Вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            task_integer2()
        elif choice == "2":
            task_real2()
        elif choice == "3":
            task_boolean3()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()

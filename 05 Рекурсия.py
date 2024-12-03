"""
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить
в табличной форме. Обязательное требование – минимизация времени выполнения и объема памяти.
Вариант 17. 17.	F(0) = 1, F(1) = 1, F(n) = (-1)^n*(F(n–1)/n! - F(n-2) /(2n)!), при n > 1
"""

import timeit
import math

# Рекурсивная функция
def F_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (-1)**n * (F_recursive(n - 1) / math.factorial(n) - F_recursive(n - 2) / math.factorial(2 * n))

# Итеративная функция
def F_iterative(n):
    if n == 0 or n == 1:
        return 1

    F_0 = 1
    F_1 = 1
    F_n = 1
    minus = -1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        F_n = minus * (F_1 / factorial - F_0 / (factorial * i))
        F_0, F_1 = F_1, F_n

    return F_n

# Ввод значения n с клавиатуры
n = int(input("Введите значение n: "))
if (n>1):
    results = []
    print(f"{'n':<5} {'Recursive Time (s)':<20} {'Iterative Time (s)':<20} {'Recursive Result':<20} {'Iterative Result':<20}")

    # Время рекурсивного вычисления
    recursive_time = timeit.timeit(lambda: F_recursive(n), number=1)
    recursive_result = F_recursive(n)

    # Время итеративного вычисления
    iterative_time = timeit.timeit(lambda: F_iterative(n), number=1)
    iterative_result = F_iterative(n)
    
    # Сохраняем результаты
    results.append((n, recursive_time, iterative_time, recursive_result, iterative_result))

    # Выводим результаты
    print(f"{n:<5} {recursive_time:<20.6f} {iterative_time:<20.6f} {recursive_result:<20} {iterative_result:<20}")

else: print("Ошибка: n не соответсвует условию.")

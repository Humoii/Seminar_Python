# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# https://ru.wikipedia.org/wiki/Числа_Фибоначчи
# Требуется найти N-е число Фибоначчи. Напишите рекурсивную функцию.
# ОБратите внимание, что функция должна возвращать число.
# Примеры/Тесты:
# <function_name>(0) -> 0
# <function_name>(2) -> 1
# <function_name>(9) -> 34


def fib_function(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_function(n - 1) + fib_function(n - 2)


print(fib_function(0))
print(fib_function(2))
print(fib_function(9))

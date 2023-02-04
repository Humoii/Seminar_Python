# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# Примеры/Тесты:
# 5 -> в ряду Фибоначчи 5 имеет порядковый номер 6

a = int(input("Введите число: "))
if a == 0:
    print(1)
else:
    fib_prev,fib_next = 0, 1
    n = 2
    while fib_next <= a:
        if fib_next == a:
            print(f"Порядковый номер числа фибоначчи {a} это {n}")
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(f"Нет такого числа, введите другое число.")

# if a == 0:
#     print(1)
# else:
#     f_prev = 0
#     f_next = 1
#     n = 2
#     while f_next <= a:
#         if f_next == a:
#             print(n)
#             break
#         f_tmp = f_prev + f_next
#         f_prev = f_next
#         f_next = f_tmp
#         n += 1
#     else:
#         print(-1)
# Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def degree(a, b):
    if b == 1:
        return a
    if b == 0:
        return 1
    if b != 1:
        return a * degree(a, b - 1)
        

print(degree(3, 4))
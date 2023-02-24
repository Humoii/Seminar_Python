# Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.
# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, 
# используя только один input, в одну строку, 
# вам понадобится распаковка и Comprehension или map


# def Generates_el_of_an_arithmetic(progression_step_amount:list)->list:
#     res = []
#     progression = progression_step_amount[0]
#     step = progression_step_amount[1]
#     amount = progression_step_amount[2]
#     for i in range(0, amount):
#         res.append(progression)
#         progression = progression + step
#     return res

# progression_step_amount = [int(input()) for i in range(3)]
# print(Generates_el_of_an_arithmetic(progression_step_amount))

# def Generates_el_of_an_arithmetic(progression:int, step:int, amount:int)->list:
#     res = []
#     for i in range(0, amount):
#         res.append(progression)
#         progression = progression + step
#     return res

def Generates_el_of_an_arithmetic(progression:int, step:int, amount:int)->list:
  
    return [progression + count * step for count in range(amount)]

progression, step, amount = map(int, input().split()) # ввод значений с разделителем пробел
print(Generates_el_of_an_arithmetic(progression, step, amount))

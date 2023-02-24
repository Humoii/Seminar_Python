# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> 
# [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

# def index_lst_rang (lst1:list, randg_min:int, randg_max:int) -> list:
#     res = []
#     count = -1
#     for i in lst1:
#         count += 1
#         if i >= randg_min and i <= randg_max:
#             res.append((count, i))
#     return res

def index_lst_rang (lst1:list, randg_min:int, randg_max:int) -> list:

    return [(idx,el) for idx, el in enumerate(lst1)if el >= randg_min and el <= randg_max]

lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
randg_min, randg_max = map(int, input().split())
print(index_lst_rang(lst1, randg_min, randg_max))
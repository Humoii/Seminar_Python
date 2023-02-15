# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку
# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

lis1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
lis2 = [3, 6, 9, 12, 15, 18]
lis1 = set(lis1)
# set - оставляет уникальные символы # он же и сортирует сразу по возрастанию
lis2 = set(lis2)
count = 0

for i in lis1:
    for j in lis2:
        if i == j:
            count += 1
            print(i, end=" ")  # end(конец)-для вывода в одну строку
if count == 0:
    print("Повторяющихся чисел нет")
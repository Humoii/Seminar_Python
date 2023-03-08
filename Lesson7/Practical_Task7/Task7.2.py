# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256
# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36
# (*) Усложнение. Сформируйте форматированный вывод с номерами строк и столбцов
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
#        1   2   3   4
#     ----------------
# 1 |    1   1   1   1
# 2 |    2   4   8  16
# 3 |    3   9  27  81
# 4 |    4  16  64 256

# print_operation_table(lambda x,y: x*y)
#        1   2   3   4   5   6
#     ------------------------
# 1 |    1   2   3   4   5   6
# 2 |    2   4   6   8  10  12
# 3 |    3   6   9  12  15  18
# 4 |    4   8  12  16  20  24
# 5 |    5  10  15  20  25  30
# 6 |    6  12  18  24  30  36

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = []

    for i in range(num_rows):
        a.append([0] * num_columns)

    for i in range(num_rows):
        for j in range(num_columns):
            a[i][0] = i+1

    for i in range(num_rows):
        for j in range(num_columns):
            a[i][j] = operation(a[i][0], a[j][0])

    print('\t', *range(1, num_columns+1), sep='\t')
    print('\t', '-'*num_columns*8)

    for i, row in enumerate(a):
        print(i + 1, '|',*row,'\n', sep ='\t')


print_operation_table(lambda x,y: x**y,4 ,4)
print_operation_table(lambda x,y: x*y)

# def print_operation_table(operation, num_rows=6, num_columns=6):

#     # Формирование таблицы
#     table = []
#     for i in range(1, num_rows+1):
#         table.append([operation(i, j) for j in range(1, num_columns+1)])

#     # Отрисовка таблицы
#     print('\t', *range(1, num_columns+1), sep='\t')
#     print('\t', '-'*num_columns*9)
#     for i, row in enumerate(table):
#         print(i+1, '|',*row,'\n', sep='\t')


# print("Таблица степеней:")
# print_operation_table(lambda x, y: x**y, 4, 4)

# print("\nТаблица умножения:")
# print_operation_table(lambda x, y: x*y, 6, 6)

def print_operation_table(operation, num_rows=6, num_columns=6) -> None:
    print('    ', end = ' ')
    for i in range(num_rows):
        print(str(i + 1).rjust(5), end = ' ')
    print('\n','   ', '- '*num_columns * 3)
    for i in range(1, num_rows+1):
        print(i, '|',end =' ')
        for j in range(1, num_columns + 1):
            print(' ',str(operation(i,j)).rjust(4),end='')
        print()


print("Таблица степеней:")
print_operation_table(lambda x, y: x**y, 4, 4)

print("\nТаблица умножения:")
print_operation_table(lambda x, y: x*y, 6, 6)
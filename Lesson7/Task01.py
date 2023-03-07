# Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], 
#                                        ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. 
# Сформировать путь к нему с использованием
# os.path и pathlib

from pathlib import Path
MAIN_DIR = Path(__file__).parent

with open(MAIN_DIR / "data" /"data.txt", mode = "r", encoding = "utf-8") as file_read:
    result = []
    for line in file_read:
        tmp = line.strip().split('#')
        result.append(tmp)
        print(*tmp)

# file_read = open('Lesson7\\data\\data.txt', mode = 'r', encoding = 'utf-8')
# result = []
# for line in file_read:
#     tmp = line.strip().split('#')
#     result.append(tmp)
#     print(*tmp)# *-распаковка
# file_read.close()

# with open('.\\Lesson7\\data\\data.txt', mode = 'r', encoding ='utf-8') as file_read:
#     result = []
#     for line in file_read:
#         tmp = line.strip().split('#')
#         result.append(tmp)
#         print(*tmp)# *-распаковка


# file_read = open("data.txt", mode = "r", encoding="utf-8")
# result = []
# for line in file_read:
#     tmp = line.strip().split('#')
#     result.append(tmp)
#     print(*tmp)
# file_read.close()



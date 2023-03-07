# Продолжение предыдущей задачи
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) 
# подобных спецификаций может быть много. 
# Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым

from pathlib import Path
MAIN_DIR = Path(__file__).parent

with open(MAIN_DIR / "data" /"data.txt", mode = "r", encoding = "utf-8") as file_read:
    result = []
    for line in file_read:
        tmp = line.strip().split('#')
        result.append(tmp)
        print(*tmp)
print('*'*25)
with open(MAIN_DIR / "data" /"res1.txt", mode = "w", encoding = "utf-8") as file_write1:
    with open(MAIN_DIR / "data" /"res2.txt", mode = "w", encoding = "utf-8") as file_write2:
        for surname, name, parent in result:
            template1 = f"{surname} {name[0]}. {parent[0]}.\n"
            template2 = f"{surname} -{name[0]} -{parent[0]}\n"
            file_write1.write(template1)
            file_write2.write(template2)

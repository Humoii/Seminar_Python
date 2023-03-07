# Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# преобразовать его в списки вида
# 1) ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# 2) ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...]
# с использованием Comprehension; Comprehension + функция; Comprehension + lambda; map
# [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы,
# в которых первая буква П

lst = [['Иванов', 'Иван', 'Иванович'], 
       ['Петров', 'Петр', 'Петрович'], 
       ['Соколов', 'Илья', 'Григорьевич']]

def template1(man):
    surname, name, parent = man
    return f"{surname} {name[0]}. {parent[0]}."

def filter1(man):
    surname, name, parent = man
    if surname[0] == 'П': return True
    return False

lst2 = [f"{man[0]} {man[1][0]}. {man[2][0]}." for man in lst]
lst3 = [f"{surname} {name[0]}. {parent[0]}." for surname, name, parent in lst]
lst4 = [template1(man) for man in lst]
lst5 = [(lambda surname, name, parent: f"{surname} {name[0]}. {parent[0]}.")
        (surname, name, parent) for surname, name, parent in lst]
lst6 = list(map(template1, lst))

print(f"{lst2}\n{lst3}\n{lst4}\n{lst5}\n{lst6}")
print('*'*50)
lst7 = [f"{man[0]} {man[1][0]}. {man[2][0]}." for man in lst if man[0][0] == 'П']
lst8 = [f"{surname} {name[0]}. {parent[0]}." for surname, name, parent in lst if surname[0] == "П"]
lst9 = [template1(man) for man in lst if man[0][0] == "П"]
lst10 = [(lambda surname, name, parent: f"{surname} {name[0]}. {parent[0]}.")
        (surname, name, parent) for surname, name, parent in lst if surname[0][0] == 'П']
lst11 = list(map(template1, filter(filter1, lst)))


print(f"{lst7}\n{lst8}\n{lst9}\n{lst10}\n{lst11}")
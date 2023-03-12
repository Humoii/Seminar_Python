# №8.1[49]. Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, 
# занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: 
# по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, 
# заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller


id_client = 0
phone_book = {}

def menu(data: dict, id_client: int):
    while True:
        print('Выберите действие: ')
        print('1 - создать новую запись')
        print('2 - распечатать содержимое справочника')
        print('3 - импортировать данные с текстового файла')
        print('4 - записать данные в текстовый файл')
        print('5 - удалить все данные')
        print('6 - удалить выбранную запись')
        print('7 - поиск в телефонной книге')
        print('8 - заменить определенную запись')
        get = input('Введите действие: ')
        if get == '':
            print('До свидания!')
            break
        elif get == '1':
            data = create(data, id_client, get_data())
        elif get == '2':
            print_phone_book(data)
        elif get == '3':
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data, id_client)
        elif get == '4':
            name_file = get_file_name()
            recording(data, name_file)
        elif get == '5':
            data = delite_everything(data)
        elif get == '6':
            number_id = int(input('Введите номер записи: '))
            data = delite_entry(data, number_id)
        elif get == '7':
            search = str(input('Введите данные по поиску: '))
            print(*search_phone_book(data, search))
        elif get == '8':
            number_id = int(input('Введите номер записи: '))
            data = delite_entry(data, number_id)
            data = create(data, id_client, get_data())
        else:
            print('Некорректный ввод данных, введите ещё раз: ')

def search_phone_book(data: dict, search: str) -> dict: #Поиск отдельной записи
        
    data1 = []
    for i in range(len(data)):
        for el in data[i+1]:
            if search.lower() in str(el).lower():
                data1.append(i+1)
                data1.append(data[i+1])
                data1.append('\n')
    lst1 = []
    for i in data1:
        if i not in lst1:
            lst1.append(i)
    return lst1

def create(data: dict, id: int, elem: tuple) -> dict: # добавляет запись в существующую телефонную книгу

    id = len(data) + 1
    data[id] = elem
    return data

def delite_entry(data: dict, number_id: int) -> dict: # удаляет выбранную запись в программе
    
    data1 = {}
    count = 0
    for key, values in data.items():
        if key != number_id:
            count += 1
            data1[count] = (values)
    return data1

def delite_everything(data: dict) -> dict: # удаляет все записи в программе
    
    data = {}
    return data

def recording (data: dict, name_file: str) -> None: # запись данных с программы в файл
    
    data1 = []
    lst = []
    for key, values in data.items():
        data1.append(values)
    for i in data1:
        lst.append("#".join(i))
    lst.append('\n')

    lst1 = []
    for i in lst:
        if i not in lst1:
            lst1.append(i)

    with open(name_file, mode = 'w', encoding = 'utf-8') as data:
        for i in lst1:
            data.writelines(i)

def print_phone_book(data: dict) -> None: # печатает данные из программы в терменале
    
    for key, values in data.items():
        print(f'Идентификатор: {key}, {values}')

def get_data() -> tuple: # запрашивает данные у пользователя для записи
    
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return (surname, name, phone, discription)

def get_file_name() -> str:
    
    return input('Введите имя файла: ')

def get_batch_data(name_file:str) -> list: # записывает данные с файла в программу
    
    lst = []
    with open(name_file, mode ='r', encoding='utf-8') as file:
        for line in file:
            temp = tuple(line.split('#'))
            lst.append(temp)
    lst = set(lst)
    return lst

def batch_create(data: dict, batch_data, id_client) -> dict: # создает id клиентов

    for elem in batch_data:
        data = create(data, id_client, elem)
    return data

menu(phone_book, id_client)
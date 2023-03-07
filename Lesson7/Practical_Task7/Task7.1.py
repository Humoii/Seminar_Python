# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False
# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") ->
# True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") ->
# True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") ->
# False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") ->
# False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") ->
# True
# Примечание.
# Подумайте об эффективности алгоритма.
# Какие структуры данных будут более эффективны по скорости.
# Алгоритм должен работать так, чтобы не делать лишних проверок.
# Подумайте, возможно некоторые проверки не нужны.
# (*) Усложнение.
# Функция имеет параметр, который определяет,
# надо ли возвращать полную информацию о кол-ве гласных букв в фразах.
# Эта информация возвращается в виде списка словарей.
# Каждый элемент списка(словарь) соответствует фразе.
# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) ->
# True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) ->
# (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") ->
# (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") ->
# (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") ->
# (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") ->
# (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])


from pathlib import Path

MAIN_DIR = Path(__file__).parent
print(MAIN_DIR)

with open(MAIN_DIR / "Vini.txt", mode="r", encoding="utf-8") as file_read:
    result = file_read.read().split("\n")

def filter_vowels(arr):
    return list(filter(lambda x: x in "аеёиоуыэюя", list(arr)))

def Count_vowels(lst):
    Vowels = ["а","е","ё","и","о","у","ы","э","ю","я"]
    arr = {}
    for i in Vowels:
        count = lst.count(i)
        if count != 0:
            arr[i] = lst.count(i)
    return arr

def Vini_ritm(result):
    for j in result:
        a = []
        b = []
        for i in j.split():
            a.append(len(filter_vowels(i)))
            b.append(Count_vowels(filter_vowels(i)))
        print((lambda arr: max(arr) == min(arr))(a), b)

Vini_ritm(result)


# def vini_rhythm_v2(line: str, info=True):

    # vowels_info = []
    # for l in line.split(): # ["пара-ра-рам", "рам-пам-папам", "па-ра-па-дам"]

    #     vowel_count = {}
    #     for i in filter(lambda x: x in "аеёиоуыэюя", l):
    #         vowel_count[i] = 1 if i not in vowel_count.keys() else vowel_count[i] + 1

    #     vowels_info.append(vowel_count)

    # vowel_count = [sum(i.values()) for i in vowels_info]
    # result = max(vowel_count) == min(vowel_count) # <-----------------------------

    # return (result, vowel_count, vowels_info) if info else result



# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
    

num = int(input("Введите число: "))

arr =  [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
diff = [abs(num - n) for n in arr]
res = [arr[i] for i, n in enumerate(diff) if n == min(diff)]

print(arr)
print(diff)
print(f"Самый близкий по значению элемент: {res}")

# num = int(input())

# arr =  [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# diff = [abs(num - n) for n in arr]
# res = [i for i, n in enumerate(diff) if n == min(diff)]

# print(num)
# print(arr)
# print(diff)

# for i in res:
#     print(i, arr[i])

# num = 6

# arr =  [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# diff = [abs(num - n) for n in arr]
# res = [(i, arr[i]) for i, n in enumerate(diff) if n == min(diff)]

# print(num)
# print(arr)
# print(diff)
# print(res)
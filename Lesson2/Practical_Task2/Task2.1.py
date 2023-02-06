# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть. 
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

Number_coins = int(input("Введите сколько монеток лежит на столе: "))
Tails = "0"
Coat_of_arms = "1"
count_coins = 1
Coint_position1 = str()
Number_of_coins_to_flip = 0
while count_coins <= Number_coins:
    Coint_position = str(input(f"Введите положение монет {Tails} - это Решкой вверх, {Coat_of_arms} - это Гербом вверх: "))
    if Coint_position != Coat_of_arms and Coint_position != Tails: print("Введите число: 0 или 1")
    else:count_coins += 1; Coint_position1 += Coint_position
for count_coins in Coint_position1:
    if count_coins == Tails: Number_of_coins_to_flip += 1
print(f"{Coint_position1}")
print(Number_of_coins_to_flip)

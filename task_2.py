# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = input('Введите трехзначное число: ')
b = 0
for i in range(3):
    b = b + int(a[i])
print('Сумма цифр: ', b)

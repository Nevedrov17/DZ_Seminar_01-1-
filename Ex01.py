#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

a = float(input("Введите число: "))
if a < 0:
    a *= -1
while a != int(a):
    a = round(a * 10, 10)
sum = 0
c = 0
while 0 < a:
    c = a % 10
    sum = c + sum
    a = a // 10
print(sum)

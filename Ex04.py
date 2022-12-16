# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число: "))
my_list = []
n = -1 * n
for i in range(n - 1, -1 * n):
    my_list.append(i + 1)
print(my_list)

poz1, poz2 = int(input('Введите первую позицию: ')), int(input('Введите вторую позицию: '))
if poz1 > len(my_list)-1 or poz2 > len(my_list)-1:
    print('Указанных позиций нет')
else:
    pr = my_list[poz1] * my_list[poz2]
    print('Произведение указанных значений =', pr)



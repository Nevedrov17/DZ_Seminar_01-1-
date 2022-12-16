import random

def mix_list(list_original):
    list = list_original[:]
    for i in range(len(list)):
        index = random.randint(0, len(list) - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

my_list = [2, 3, 4, 5, 6 ,7, 8]

print(mix_list(my_list))
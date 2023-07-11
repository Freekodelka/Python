""" Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число 
N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X """

import random

N = int(input('Введите количество элементов в списке: '))
X = int(input('Искать число в списке: '))

list_1 = [(random.randint(0, 100)) for i in range(N)]
min = abs(list_1[0]-X) 
delta_index = 0
print(list_1)
for i in range(len(list_1)):
    if (abs(list_1[i] - X)) < min:
        min = abs(list_1[i] - X)
        delta_index = i    
print('Самый близкий по величине элемент в списке: ', list_1[delta_index])
""" Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума) """

import random


def inputArray():
    n = int(input('Введите количество элементов массива: '))
    list_1 = [(random.randint(-100, 100)) for i in range(n)]
    return list_1

def find_indexes(lst, start_interval, finish_interval):
    return [i for i in range(len(lst)) if start_interval <= lst[i] <= finish_interval]

list_1 = inputArray()
n = int(input('Введите начало интервала: '))
m = int(input('Введите конец интервала: '))
print(list_1)
print(f'Индексы элементов вышеуказанного списка, находящиеся в интервале от {n} до {m}: {find_indexes(list_1, n, m)}')



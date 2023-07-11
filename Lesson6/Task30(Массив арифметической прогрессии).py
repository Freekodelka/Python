""" Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

def arithmetic_progression(a1, n, d):
    result = a1
    progression_list = []    
    for i in range(n): 
        progression_list.append(int(result))
        result += d      
        
    return progression_list


a1 = int(input('Введите первый элемент прогрессии a1: '))
n = int(input('Введите количество элементов прогрессии n: '))
d = int(input('Введите разность прогрессии d: '))
print(arithmetic_progression(a1, n, d))
    
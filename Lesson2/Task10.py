""" На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, 
которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, 
которые нужно перевернуть """

n = int(input('Введите количество монеток: ')) 
count_head = 0
count_tail = 0
for i in range(n):
    coins = int(input('head or tail: '))
    while coins < 0 or coins > 1:
        coins = int(input('Insert correct number from 0 to 1 \nhead or tail: '))  
        
    if coins == 1:         
        count_head +=1
    else:
        count_tail +=1
print('Количестdо орлов', count_head, 'Количестdо решек',count_tail, 'Необходимо перевернуть: ', count_tail)
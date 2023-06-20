""" Factorial = 1 
n = int(input('Введите целое и неотрицательное число '))
summary = 1
if n <=0:
    print('Incorrect number')
    exit()
while Factorial <= n:    
    summary *= Factorial
    Factorial +=1
print(summary) # Факториал числа """


""" n = int(input('Введите количесвто наблюдаемых дней: ')) #Ввести количество дней с клавиатуры
count = 0
for i in range(n): 
    temp = int(input('Введите показатель температуры: '))   #ввести параметры с клавиатуры равное количеству дней указанных выше
    if temp > 0:
        count +=1
print(count) """

""" # Нахождение минимальной и максимальной массы арбузов
n = int(input('Введите количество арбузов: '))
min_massa = 10**1000
max_massa = 0
for i in range(n):
    massa = int(input('Масса арбуза: '))
    if massa < min_massa:
        min_massa = massa
    if massa > max_massa:
        max_massa = massa
print('Максимальная масса: ', max_massa, 'Минимальная масса', min_massa) """

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
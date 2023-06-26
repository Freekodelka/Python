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



""" list_1 = []
for i in range(1, 101):
    list_1.append (i)
print(list_1)

list_1 = [i for i in range(1, 101)]
print(list_1) """
list_1 = [(i, i*i) for i in range(1, 101) if i % 2 == 0]
print(list_1)

""" list_1 = [(i*2) for i in range(1, 101) if i % 2 == 0]
print(list_1) """
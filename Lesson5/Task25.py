""" Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. """

def degree(a, b):    
        
    if b == 0:
        return 1
    elif b % 2 == 0:
        return degree(a*a, b//2)
    else:
        return a * degree(a, b - 1)   

    
a = int(input('Введите число А: '))
b = int(input('Введите степень числа А: '))
print(degree(a, b))  

""" Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы. """
def summary(a, b):
    if b == 0:
        return a
    else:
        return summary(a + 1, b - 1)
a = int(input('Input first number: '))
b = int(input('Input second number: '))
print('The sum of numbers = ', summary(a, b))
    
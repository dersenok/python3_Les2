#8. Вводятся три разных числа.
#Найти, какое из них является средним






print('Введите три числа: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)
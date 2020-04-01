# Функция перевода десятичного числа в двоичный формат


def binary(num):
    s = ''
    while num > 0:
        s = f'{num % 2}{s}'
        num //= 2
    return s

#

while True:
    n = int(input('Введите целое число: '))
    if n != 0:
       print(binary(n))
       print('Для завершения программы введите 0')
    else:
        break
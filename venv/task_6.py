num = int(input('Введите целое число: '))
ans = input('Перевести в байты - "b", в килобайты - "k"')

ans = ans.lower()
if ans == 'b':
    print(f'{num} КБ = {num * 1024} байт')
elif ans == 'k':
    print(f'{num} Байт = {num / 1024} КБайт')
else:
    print('Неверный ввод')
# Рекурсия
# Глубина не более  1000 вызовов

def func(a, b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'
print(func(1, 10))
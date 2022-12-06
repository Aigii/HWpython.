
from random import randint as RI

def create_pattern(min: int, max: int) -> dict:
    degree = int(input('Введите степень максимальную многочлена: '))
    equation_pattern = {}
    for key in range(degree, -1, -1):
        value = RI(min, max)
        equation_pattern[key] = value
    return equation_pattern

my_listt_first = create_pattern(1, 100)

one = []
for key, value in my_listt_first.items():
    a = f'{value}x^{key}'
    one.append(a)
result = '+'.join(one)
result = result.replace('x^1+', 'x+')
result = result.replace('x^0', '')
print(result, '= 0')

my_list_second = create_pattern(-100, 100)
two = []
for key, value in my_list_second.items():
    a = f'{value}x^{key}'
    two.append(a)
result = '+'.join(two)
result = result.replace('+-', '-')
result = result.replace('x^1+', 'x+')
result = result.replace('x^0', '')
print(result, '= 0')

first = my_listt_first
second = my_list_second

def equation_addition(first: dict, second: dict) -> dict:
    base = {}
    base.update(first)
    base.update(second)
    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])

summa = equation_addition(first, second)
three = []
for key, value in summa.items():
    a = f'{value}x^{key}'
    three.append(a)
three = ('+'.join(three))
three = three.replace('+-', '-')
three = three.replace('x^1+', 'x+')
three = three.replace('x^0', '')
print('Сумма двух многочленов:')
print(three, '= 0')

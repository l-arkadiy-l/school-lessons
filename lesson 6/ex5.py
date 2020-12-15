from math import sqrt

radius, x, y = map(int, input('Введите r, x, y через пробел: ').split())
if sqrt(x) + sqrt(y) > radius:
    print('YES')
else:
    print('NO')

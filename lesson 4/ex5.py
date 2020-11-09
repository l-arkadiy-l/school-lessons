a = int(input('Введите длину прямоугольника: '))
b = int(input('Введите ширину прямоугольника: '))
c = int(input('Введите сторону квадрата: '))
counter = 0
n = a * b
if a > c and b > c:
    while n >= c ** 2:
        n -= c ** 2
        counter += 1
print('В прямоугольнике {}х{} можно разместить {} квадратов со стороной {}'.format(a, b, counter, c))
print('Площадь незанятой части {}'.format(n))

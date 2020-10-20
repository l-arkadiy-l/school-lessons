# A·x 2 +B·x+C=0
from math import sqrt


def count_x(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    x_1 = (-b + -sqrt(discriminant)) / (2 * a)
    x_2 = (-b + sqrt(discriminant)) / (2 * a)
    return 'X1 = {:.2f}\nX2 = {:.2f}'.format(x_1, x_2)


a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))
print(count_x(a, b, c))

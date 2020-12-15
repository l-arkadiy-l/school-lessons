from math import sqrt

x = int(input('Введите x: '))
ans = None
if x <= 0:
    ans = 5 * x ** 2 + 3 * x - 2
elif x > 0:
    ans = sqrt(2 * x + 5)
print(ans)

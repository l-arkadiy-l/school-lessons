from math import pi

radius_2 = float(input('Введите радиус внутренней окружности R2 = '))
radius_1 = float(input('Введите радиус внешней окружности R1 > {:.1f}, R1 = '.format(radius_2)))
s_2 = pi * radius_2 ** 2
s_1 = pi * radius_1 ** 2
print('Площадь внутренней окружности S2 = {:.2f}'.format(s_2))
print('Площадь внешней окружности S1 = {:.2f}'.format(s_1))
print(
    'Площадь кольца, между R1 = {:.1f} и R2 = {:.1f}, S = {:.2f} – {:.2f} = {:.2f}'.format(radius_1, radius_2, s_1, s_2,
                                                                                           s_1 - s_2))

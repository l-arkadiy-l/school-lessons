from math import sqrt


def length_segment(x, y, x1, y1):
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)


point_a = list(map(float, input('Введите координаты точки A (x, y):\n').split(', ')))
point_b = list(map(float, input('Введите координаты точки B (x, y):\n').split(', ')))
print('Длина отрезка AB = {:.3f}'.format(length_segment(point_a[0], point_a[1], point_b[0], point_b[1])))
if __name__ == '__main__':
    try:
        assert length_segment(5.5, 3.5, 1.5, 2) == 4.272001872658765, print('error')
    except AssertionError:
        print('ERROR')

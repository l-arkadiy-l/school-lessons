k = int(input('Введите целое число К, 1 < K < 365: '))
print('a) номер дня недели {}'.format(k % 7))
print('b) номер дня недели {}'.format((k + 3) % 7))
print('c) номер дня недели {}'.format((k + 5) % 7))

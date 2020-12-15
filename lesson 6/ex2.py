year1, year2 = map(int, input('Введите два числа: ').split())
if year1 < year2:
    print('FIRST')
elif year1 > year2:
    print('SECOND')
else:
    print('SAME')

print('Пример: ')
class_1, class_2, class_3 = list(map(int, input('Введите число учащихся в трех классах: ').split(', ')))
# class_1 // 2 - 2 ученика за партой
# class_1 % 2 - однин ученик за партой
print('Закупить {} парт'.format(class_1 // 2 + class_1 % 2 + class_2 // 2 + class_2 % 2 + class_3 // 2 + class_3 % 2))

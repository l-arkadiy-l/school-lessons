print('Пример:')
number = int(input('Введите число: '))
number_system = int(input('Введите основание системы счисления: '))
newNum = 0
for i in range(len(str(number)) - 1, -1, -1):
    newNum += int(str(number)[i]) * number_system ** i
print('Число {} это аналог числа {} в системе счисления с основанием {}'.format(newNum, number, number_system))

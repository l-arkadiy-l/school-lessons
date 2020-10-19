numbers = list(map(int, input().split()))


def multiply_numbers(number_1, number_2, number_3, string):
    sum_numbers = sum([number_1, number_2, number_3])
    if string == '/':
        return sum_numbers / 3
    elif string == '+':
        return sum_numbers
    else:
        return number_1 * number_2 * number_3


print('{}+{}+{}={}'.format(numbers[0], numbers[1], numbers[-1],
                           sum(numbers)))
print('{}*{}*{}={}'.format(numbers[0], numbers[1], numbers[-1],
                           multiply_numbers(numbers[0],
                                            numbers[1], numbers[-1], '*')))
print('({}+{}+{}) / 3={}'.format(numbers[0], numbers[1], numbers[-1],
                                 multiply_numbers(numbers[0],
                                                  numbers[1],
                                                  numbers[-1], '/')))
print('({}+{}+{}) / 3={:.3f}'.format(numbers[0], numbers[1], numbers[-1],
                                     multiply_numbers(numbers[0],
                                                      numbers[1],
                                                      numbers[-1], '/')))

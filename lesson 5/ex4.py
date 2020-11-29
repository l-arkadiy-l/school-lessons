def check_triangular(a, b, c, check_90=True):
    list_nums = [a, b, c]
    a = min(list_nums)
    del list_nums[list_nums.index(a)]
    if check_90:
        return min(list_nums) ** 2 + a ** 2 == max(list_nums)
    else:
        return min(list_nums) + a > max(list_nums)


a, b, c = int(input()), int(input()), int(input())
print('{} == {} == {} -- {}'.format(a, b, c, a == b == c))
print('{} == {} or {} == {} or {} == {} -- {}'.format(a, b, a, c, b, c, a == b or a == c or b == c))
print('check_triangular({}, {}, {}) -- {}'.format(a, b, c, check_triangular(a, b, c)))
print(
    '{} + {} > {} and {} + {} > {} and {} + {} > {} -- {}'.format(a, b, c, b, c, a, a, c, b,
                                                                  check_triangular(a, b, c, False)))

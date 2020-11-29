def one_positive(a, b, c):
    list_nums = [a, b, c]
    if min(list_nums) > 0:
        return False
    del list_nums[list_nums.index(min(list_nums))]
    if min(list_nums) < 0 and max(list_nums) >= 0:
        return True
    return False


def two_positive(a, b, c):
    list_nums = [a, b, c]
    if min(list_nums) > 0:
        return False
    del list_nums[list_nums.index(min(list_nums))]
    if list_nums[0] >= 0 and list_nums[-1] >= 0:
        return True
    return False


a, b, c = int(input()), int(input()), int(input())
print('{} < {} < {} -- {}'.format(a, b, c, a < b < c))
print('{} >= 0 and {} >= 0 and {} >= 0 -- {}'.format(a, b, c, a >= 0 and b >= 0 and c >= 0))
print('one_positive({}, {}, {}) -- {}'.format(a, b, c, one_positive(a, b, c)))
print('two_positive({}, {}, {}) -- {}'.format(a, b, c, two_positive(a, b, c)))

a, b = int(input()), int(input())
print('{} > 2 and {} <= 3 -- {}'.format(a, b, (a > 2 and b <= 3)))
print('{} % 2 == 0 or {} != {} -- {}'.format(a, a, b, a % 2 == 0 or a != b))
print('{} % 5 == 0 and ({} - {}) % {} != 0 -- {}'.format(a, a, b, b, a % 5 == 0 and (a - b) % b != 0))
print('{} % 2 != 0 and {} % 2 != 0 -- {}'.format(a, b, a % 2 != 0 and b % 2 != 0))
print('({} % 2 != 0 and {} % 2 == 0) or ({} % 2 != 0 and {} % 2 == 0)'.format(a, b, b, a, (
            (a % 2 != 0 and b % 2 == 0) or (b % 2 != 0 and a % 2 == 0))))
print('{} % {} == 0 -- {}'.format(max(a, b), min(a, b), (a % b == 0 or b % a == 0)))

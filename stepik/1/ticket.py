n = int(input())
first = n // 1000
second = n % 1000


def sum_digits(np):
    nn = np
    sumd = 0
    l = len(str(np))
    for x in reversed(range(l)):
        # print('x', x)
        sumd = sumd + nn // (10 ** x)
        # print('sumd', sumd)
        nn = nn % (10 ** x)
        # print('nn', nn, '\n')
    return sumd


# print(first, sum_digits(first))
# print('\n\n-------------\n')
# print(second, sum_digits(second))

if sum_digits(first) == sum_digits(second):
    print('Счастливый')
else:
    print('Обычный')

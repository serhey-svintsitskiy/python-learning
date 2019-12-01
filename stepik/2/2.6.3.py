lst = list(map(int, input().split()))
x = int(input())

if lst.count(x) == 0:
    print('Отсутствует')
else:
    l = []
    for i in range(len(lst)):
        if lst[i] == x:
            l.append(str(i))
    print(' '.join(l))


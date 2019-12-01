l = [int(i) for i in input().split()]
if len(l) < 2:
    n = l
else:
    n = []
    i = 0
    while i < len(l):
        if i == 0:
            left = l[-1]
        else:
            left = l[i-1]
        if i == len(l) - 1:
            right = l[0]
        else:
            right = l[i+1]
        t = left + right
        n.append(t)
        i += 1
print(' '.join(map(str, n)))


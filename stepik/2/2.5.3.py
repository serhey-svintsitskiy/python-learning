l = sorted([int(i) for i in input().split()])
r = []
for el in l:
    if l.count(el) > 1 and el not in r:
        r.append(el)
print(' '.join(map(str, r)))


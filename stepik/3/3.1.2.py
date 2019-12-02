l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

i = 0
while i < len(l):
    if l[i] % 2 != 0:
        l.pop(i)
    else:
        l[i] = l[i] // 2
        i += 1
    print(l)
print(l)

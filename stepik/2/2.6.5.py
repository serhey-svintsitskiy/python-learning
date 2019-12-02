def sq(st, n, result, rn, cn):
    if n == 1:
        result[cn][rn] = st + 1
        n = 0
    if n < 1:
        return result
    curr = st
    for i in range(n - 1):
        curr = curr + 1
        result[cn][rn + i] = curr
    for i in range(n - 1):
        curr = curr + 1
        result[cn + i][rn + n - 1] = curr
    for i in range(n - 1):
        curr = curr + 1
        result[cn + n - 1][rn + n - 1 - i] = curr
    for i in range(n - 1):
        curr = curr + 1
        result[cn + n - 1 - i][rn] = curr
    sq(curr, n - 2, result, rn + 1, cn + 1)


# n = int(input())
n = 10
result = [[0 for i in range(n)] for j in range(n)]

sq(0, n, result, 0, 0)

for i in range(len(result)):
    print(' '.join([str(j) for j in result[i]]))

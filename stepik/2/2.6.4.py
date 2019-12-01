def summatrix(m, i, j):
    row = m[i]
    column = []
    for listrow in m:
        column.append(listrow[j])
    bottom = column[i - len(column) + 1]
    top = column[i - 1]
    left = row[j - 1]
    right = row[j - len(row) + 1]
    # print('''i, j, bottom + top + left + right,''', bottom, top, left, right)
    return bottom + top + left + right


'''
matrix = []
s = input()
while s != 'end':
    matrix.append(list(map(int, s.split())))
    s = input()
'''

matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]

for i in range(len(matrix)):
    newRow = []
    for j in range(len(matrix[i])):
        newRow.append(str(summatrix(matrix, i, j)))
    print(' '.join(newRow))

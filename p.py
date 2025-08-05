matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

n = len(matrix1)
result = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

for items in result:
    print(items)
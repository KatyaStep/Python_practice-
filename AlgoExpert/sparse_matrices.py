

matrix_a = [
    [0, 2, 0],
    [0, -3, 5]
]

matrix_b = [
    [0, 10, 0],
    [0, 3, 0],
    [0, 0, 4],
]

row_a = len(matrix_a)
col_a = len(matrix_a[0])

row_b = len(matrix_b)
col_b = len(matrix_b[0])

output_matrix = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

if col_a == row_b:
    for i in range(row_a):
        for k in range(row_b):
            if matrix_a[i][k] != 0:
                for j in range(col_b):
                    output_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
else:
    print([[]])

print(output_matrix)
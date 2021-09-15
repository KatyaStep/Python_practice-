def sparse_matrix(matrix_a, matrix_b):
    row_a = len(matrix_a)
    row_b = len(matrix_b)

    col_a = len(matrix_a[0])
    col_b = len(matrix_b[0])

    if col_a != row_b:
        return [[]]

    output_matrix = [[0] * col_b for _ in range(row_a)]

    no_sparse_a = non_zero_dict(matrix_a)
    no_sparse_b = non_zero_dict(matrix_b)

    # print(output_matrix)
    # print(no_sparse_a)
    # print(no_sparse_b)

    for key_a, value_a in no_sparse_a.items():
        for key_b, value_b in no_sparse_b.items():
            if key_a[1] == key_b[0]:
                output_matrix[key_a[0]][key_a[1]] += no_sparse_a.get(key_a) * no_sparse_b.get(key_b)

    return output_matrix


def non_zero_dict(matrix):
    non_zero_val = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                non_zero_val[i, j] = matrix[i][j]

    return non_zero_val

if __name__ == '__main__':
    matrix_a = [
        [0, 2, 0],
        [0, -3, 5]
    ]

    matrix_b = [
        [0, 10, 0],
        [0, 0, 0],
        [0, 0, 4],
    ]

    print(sparse_matrix(matrix_a, matrix_b))
    # print(non_zero_dict(matrix_a, matrix_b))
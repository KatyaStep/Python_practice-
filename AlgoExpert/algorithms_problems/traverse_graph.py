def number_of_ways_to_traverse_graph(width, height):
    matrix = create_matrix(width, height)
    print(matrix)
    # change_first_row(matrix)
    # print_distance(matrix, width, height)
    # print()
    traverse_graph(matrix, width, height)
    # print_distance(matrix, width, height)
    print(matrix)


def create_matrix(width, height):
    """Create a matrix"""
    matrix = []
    for row in range(height+1):
        matrix.append([])
        for column in range(width+1):
            matrix[-1].append(0)

    return matrix


def print_distance(matrix, rows, columns):
    """Print out a matrix"""
    for pos_1 in range(columns+1):
        for pos_2 in range(rows+1):
            print(int(matrix[pos_1][pos_2]), end=" ")
        print()


def change_first_row(matrix):
    """Change a first row in the matrix"""
    for first_row_el in range(len(matrix[0])):
        matrix[0][first_row_el] = 1

    for first_col_el in range(len(matrix)):
        matrix[first_col_el][0] = 1

    return matrix


def traverse_graph(matrix, width, height):
    # rows = len(matrix)
    # columns = len(matrix[0])

    for row in range(1, width+1):
        for column in range(1, height+1):
            if row == 0 or column == 1:
                matrix[column][row] = 1
            else:
                matrix[column][row] = matrix[column][row - 1] + matrix[column-1][row]

    return matrix


number_of_ways_to_traverse_graph(4, 3)

"""Module Doc String"""
# import numpy


def levenshtein_distance(str1, str2):
    """Returns the minimum number of edit operations that need to perform
    on the first string to obtain the second string"""

    # "Case with using a numpy"
    # distances = numpy.zeros((len(str1)+1, len(str2)+1))

    number_of_rows = len(str1) + 1
    number_of_columns = len(str2) + 1

    distances = create_matrix(number_of_rows, number_of_columns)
    change_column_row_matrix(str1, str2, distances)
    calculate_distance(str1, str2, distances)
    print_distance(distances, len(str1)+1, len(str2)+1)
    print()

    return int(distances[-1][-1])


def create_matrix(row_count, col_count):
    """Create a matrix with zeroes"""
    matrix = []
    while len(matrix) < row_count:
        matrix.append([])
        while len(matrix[-1]) < col_count:
            matrix[-1].append(0)

    return matrix


def change_column_row_matrix(str1, str2, matrix):
    """Change zeroes in a first row and column on numbers"""
    for pos_1 in range(len(str1)+1):
        matrix[pos_1][0] = pos_1

    for pos_2 in range(len(str2)+1):
        matrix[0][pos_2 ] = pos_2

    return matrix


def print_distance(distances, str1_length, str2_length):
    """Print out a matrix"""
    for pos_1 in range(str1_length):
        for pos_2 in range(str2_length):
            print(int(distances[pos_1][pos_2]), end=" ")
        print()


def calculate_distance(str1, str2, matrix):
    """Calculate a difference between two strings"""
    for pos_1 in range(1, len(str1)+1):
        for pos_2 in range(1, len(str2)+1):
            if str1[pos_1-1] == str2[pos_2-1]:
                matrix[pos_1][pos_2] = matrix[pos_1-1][pos_2-1]
            else:
                first_var = matrix[pos_1-1][pos_2] + 1
                second_var = matrix[pos_1][pos_2-1] + 1
                third_var = matrix[pos_1-1][pos_2-1] + 1
                matrix[pos_1][pos_2] = min(first_var, second_var, third_var)

    return matrix


print(levenshtein_distance("abc", "ybcd"))

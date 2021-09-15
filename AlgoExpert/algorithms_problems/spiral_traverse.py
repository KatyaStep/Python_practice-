def spiralTraverse(array):
    start_row = 0
    start_column = 0
    end_row = len(array) - 1
    end_column = len(array[start_row]) - 1
    spiral_order = []

    while start_row <= end_row and start_column <= end_column:
        for i in range(start_column, end_column+1):
            spiral_order.append(array[start_row][i])

        for j in range(start_row+1, end_row):
            spiral_order.append(array[j][end_column])

        for k in range(end_column, start_column, -1):
            if start_row == end_row:
                break
            spiral_order.append(array[end_row][k])

        for l in range(end_row, start_row, -1):
            if start_column == end_column:
                break
            spiral_order.append(array[l][start_column])


        start_row += 1
        start_column += 1
        end_row -= 1
        end_column -= 1

    return spiral_order


# my_array = [
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
#     [7]
# ]

my_array = [
    [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
    ]


# my_array = [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
# ]

# my_array = [
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]

# my_array = [
#     [27, 12, 35, 26],
#     [25, 21, 94, 11],
#     [19, 96, 43, 56],
#     [55, 36, 10, 18],
#     [96, 83, 31, 94],
#     [93, 11, 90, 16]
#   ]

print(spiralTraverse(my_array))

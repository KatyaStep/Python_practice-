
def diagonal_output():
    board = [
            [1, 2, 3, 4],
            [8, 9, 10, 5],
            [11, 12, 13, 6]
    ]

    row_number = len(board)
    col_len = len(board[0])

    # print("Row_number: ", row_number)
    # print("Col length: ", col_len)
    i = 0
    j = 0
    start_col = 0
    start_row = 0

    while True:

        print(board[i][j])

        i += 1
        j += 1

        # if j == col_len - 1:
        if i >= row_number or j >= col_len:
            start_col += 1
            j = start_col
            i = start_row
            print()

        # if start_col == col_len:
        #     start_row += 1
        #     i = start_row
        #     j = 0
        #     start_col = 0

        if start_col + start_row >= col_len and j >= col_len:
            start_row += 1
            start_col = 0
            i = start_row
            j = start_col
            print()

        if start_row == row_number:
            break



#     max_col = len(test[0])
#     max_row = len(test)
#     cols = [[] for _ in range(max_col)]
#     rows = [[] for _ in range(max_row)]
#     fdiag = [[] for _ in range(max_row + max_col - 1)]
#     bdiag = [[] for _ in range(len(fdiag))]
#     min_bdiag = -max_row + 1

#     for x in range(max_col):
#         for y in range(max_row):
#             cols[x].append(test[y][x])
#             rows[y].append(test[y][x])
#             fdiag[x+y].append(test[y][x])
#             bdiag[x-y-min_bdiag].append(test[y][x])

#     print(fdiag, end='\n')
#             #print(bdiag)

diagonal_output()

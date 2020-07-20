
# VS review
# Todo:
# - fix code style
# - remove commnets
# - add doc string to function
# - don't use variables shorter than 4 letters
# - On the command line run python3 -m pylint <name of this file>

figures = {
    'wpawn':'8', # VS: make value a int
    'wknight':'2',
    'wbishop':'2',
    'wrook': '2',
    'wqueen': '1',
    'wking': '1',
    'bpawn':'8',
    'bknight':'2',
    'bbishop':'2',
    'brook': '2',
    'bqueen': '1',
    'bking': '1'
}

chess_board = ['a','b','c', 'd', 'e', 'f', 'g', 'h']

board_for_validation = {'2b':'wking', '8c':'bking', '4d':'wpawn'}


def valid_board(board):
    message = ""
    for k, v in board.items():
        if v in figures:
            if figures[v] != '0':
                figures[v] = str(int(figures[v]) - 1)
                if (int(k[0]) < 9) and (k[1] in chess_board):  # VS: use variables for k[0] k[1]
                    message = "That's a correct board"  # VS: fix indentation
                else:
                    message = "That's not a correct board"
                    break
            else:
                message = "You have incorrect board"
                break
        else:
            message = "That's not a correct board "
            break

    return print(message)


valid_board(board_for_validation)

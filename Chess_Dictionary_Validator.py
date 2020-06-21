
figures = {
    'wpawn':'8',
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
    'bking': '1,'
}

chess_board = ['a','b','c', 'd', 'e', 'f', 'g', 'h']

board_for_validation={'wpawn':'2b', 'wking':'4c'}
message=''

def valid_board (board):
    for k, v in board.items():
        if k in figures:
            for item in chess_board:
                for digit in range (1,9):
                    if str(digit) + str(item) == v:
                        message = "That's a correct board"
        else:
            message = "That's not a correct board "
        
        return print(message)

valid_board(board_for_validation)
# TO DO:
"""
* Done - Create the board size 7 columns x 6 rows
* Done - Create players
* Done - Choose color for players
* Done - while not find winner:
* Done - Make turn
* Done - Toggle player
* find winner
* show final board
"""


def main(board):
    show_header()

    players = ['Kate', 'Computer']
    colors = ['R', 'B']
    index_player = 0

    while not find_winner(board, colors):
        player = players[index_player]
        color = colors[index_player]

        announce_turn(player)
        show_board(board)

        if not choose_location(board, color):
            print("It's not an option. Try Again")
            continue

        index_player = (index_player+1) % 2

    return True


def announce_turn(player):
    print()
    print(f"{player}, your turn")
    print()


def choose_location(board, color):
    row = int(input("Choose row:"))
    column = int(input("Choose column:"))

    row -= 1
    column -= 1

    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False

    cell = board[row][column]

    if cell != 'None':
        return False

    board[row][column] = color
    return True


def find_winner(board, colors):
    sequence = []
    winner_score = 4
    # winner row
    for row in board:
        for cell in range(len(board[0])):
            if row[cell] in colors:
                if row[cell] in sequence:
                    sequence.append(row[cell])
                else:
                    sequence = [row[cell]]
            else:
                sequence = []

        if len(sequence) >= winner_score:
            return True

    # winner column
    rows = len(board) - 1

    # print(row, col)

    for col in range(len(board[0])):
        for row in range(rows):
            print(board[row][col])

            if board[row][col] in colors:
                if board[row][col] in sequence:
                    sequence.append(board[row][col])
                else:
                    sequence = [board[row][col]]
            else:
                sequence = []

        if len(sequence) >= winner_score:
            return True

    return False


def show_header():
    print("------------------")
    print('Game "Connect 4"')
    print("------------------")


def show_board(board):
    # Create a board of size (7 col x 6 rows)
    for row in board:
        for cell in row:
            symbol = cell if cell != 'None' else '_'
            print(symbol, end='|')
        print()

    return board


if __name__ == "__main__":
    board = [
        ['None', 'None', 'None', 'R', 'B', 'R', 'R'],
        ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
        ['None', 'None', 'None', 'None', 'None', 'None', 'None'],
    ]
    main(board)

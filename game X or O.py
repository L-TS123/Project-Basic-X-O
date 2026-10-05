from my_functions import *
while True:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
        ]
    print_board(board)
    while True:
        valid_square(board, player="X")

        if winner("X", board) == "The X is a winner!":
            print(f'The X is a winner!')
            break

        if check_full_board(board) == 'Tie':
            print('Tie')
            break

        valid_square(board, player = "O")

        if winner("O", board) == "The O is a winner!":
            print(f'The O is a winner!')
            break

        if check_full_board(board) == 'Tie':
            print('Tie')
            break

    if play_again() == False:
            break









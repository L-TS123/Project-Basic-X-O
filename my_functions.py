from typing import overload

def match_square(square):
    match square:
        case 1:
            return 0,0
        case 2:
            return 0,1
        case 3:
            return 0,2
        case 4:
            return 1,0
        case 5:
            return 1,1
        case 6:
            return 1,2
        case 7:
            return 2,0
        case 8:
            return 2,1
        case 9:
            return 2,2


def square_occupied(square, board):
    pos = match_square(square)
    return board[pos[0]][pos[1]] != " "


def print_board(board):
    for row in board:
        print (" | ".join(row))
        print("-" * 9)


def make_move(square, board, player):
    pos = match_square(square)
    board[pos[0]][pos[1]] = player
    print_board(board)


def valid_square(board, player):
    while True:
        try:
            square = int(input("Enter a number between 1-9:"))
        except:
            print("Invalid number")
            continue
        if square > 9 or square < 1:
            print("Invalid number")
            continue
        else:
            if (square_occupied(square, board) == False):
                make_move(square, board, player)
                break
            else:
                print("Square occupied")


def winner(player, board):
    for i in board:
        total = 0
        for j in i:
            if j == player:
                total += 1
        if total == 3:
            return f'The {player} is a winner!'
        if board[0][0] == board[1][0] == board[2][0] == player:
            return f'The {player} is a winner!'
        if board[0][1] == board[1][1] == board[2][1] == player:
            return f'The {player} is a winner!'
        if board[0][2] == board[1][2] == board[2][2] == player:
            return f'The {player} is a winner!'
        if board[0][0] == board[1][1] == board[2][2] == player:
            return f'The {player} is a winner!'
        if board[0][2] == board[1][1] == board[2][0] == player:
            return f'The {player} is a winner!'


def check_full_board(board):
    board_full = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                board_full = False
                break
    if board_full:
        return "Tie"


def play_again():
    again = input("Play again?(Yes/No)")
    if again.lower() == "yes":
        return True
    else:
        print("Good bye")
        return False







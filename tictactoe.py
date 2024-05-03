game_score = {}

def players_names():
    player_1 = input("Enter first player's name: ")
    player_2 = input("Enter second player's name: ")

    game_score[player_1] = 0
    game_score[player_2] = 0

    return player_1, player_2


def score(winner):
    game_score[winner] += 1


def game_score_print():
    print('Actual game score:')

    for key, value in game_score.items():
        print(f'{key} : {value}')


def board_draw(board):
    for row in board:
        row_view = f"{' | '.join(row)} |"
        print(row_view)
        print('------------------')
    print()


def greeting():
    print(f"Hello! \n"
          f"Here is 'Noughts an crosses' game. \n"
          f"RULES: To make your move, you need \n"
          f"to enter the coordinates of the cell: \n"
          f"first horizontally (X), \n"
          f"second vertically (Y)! \n"
          f"Separate entered coordinates with SPACE! \n"
          f"Enter gamers's names: \n"
          f"First one will play for X and second one \n"
          f"will play for O. \n"
          f"Let's play! \n"
          "--------------------------------------")


def move(board):
    while True:
        coordinates = input(('Enter coordinates for move: ')).split()

        if len(coordinates) > 2 or len(coordinates) < 2:
            print('Please enter TWO coordinates!')
            continue

        x, y = coordinates

        if not x.isdigit() or not y.isdigit():
            print('Please enter NUMERIC value for coordinates!')
            continue

        x, y = int(x), int(y)

        if x not in range(1, 4) or y not in range(1, 4):
            print('Please enter coordinates from correct RANGE!')
            continue

        if board[x][y] != " ":
            print('Enter coordinates of FREE cell!')
            continue

        return x, y


def check_win(board):
    win_comb = (
        ((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)),
        ((1, 1), (2, 1), (3, 1)), ((1, 2), (2, 2), (3, 2)), ((1, 3), (2, 3), (3, 3)),
        ((1, 1), (2, 2), (3, 3)), ((1, 3), (2, 2), (3, 1))
    )
    for comb in win_comb:
        combination = []

        for a in comb:
            combination.append(board[a[0]][a[1]])

        if combination == ['X', 'X', 'X']:
            print(f'Crosses win!')
            board_draw(board)
            return True

        if combination == ['0', '0', '0']:
            print('Noughts win!')
            board_draw(board)
            return True

    return False

def play():
    while True:
        board = [[' ' for j in range(4)] for i in range(4)]

        board[0][0] = 'X|Y'
        board[0][1], board[1][0] = '1', '  1'
        board[0][2], board[2][0] = '2', '  2'
        board[0][3], board[3][0] = '3', '  3'

        game(board)

        print('Do you want to play one more time?')
        play_again = input('Press Y or N: ').lower()

        if play_again not in ('y', 'yes'):
            print('Thank you for playing!')
            break


def game(board):
    count_move = 0

    while True:

        count_move += 1

        board_draw(board)

        if count_move % 2 == 1:
            print(f"{player_1}'s turn for X!")
        else:
            print(f"{player_2}'s turn for O!")

        x, y = move(board)

        if count_move % 2 == 1:
            board[x][y] = 'X'
        else:
            board[x][y] = '0'

        if check_win(board):
            if count_move % 2 == 1:
                score(player_1)
            else:
                score(player_2)

            game_score_print()

            break


        if count_move == 9:
            print('Game draw!')
            game_score_print()

            break




greeting()
player_1, player_2 = players_names()
play()




from utils import render, get_winner,is_board_full,make_move,is_a_valid_move
import ai
import sys

def new_board():
    empty_board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    return empty_board

def get_human_move(board, player):
    inputs = []
    inputs.append(int(raw_input("What is your move's X co-ordinate?:")))
    inputs.append(int(raw_input("What is your move's Y co-ordinate?:")))
    return tuple(inputs)

def get_player_move(player_type, player, board):
    
    if player_type == 'human':
        return get_human_move(board, player)
    elif player_type == 'random_ai':
        return ai.random_ai(board, player)
    elif player_type == 'winning_ai':
        return ai.finds_winning_and_losing_moves_ai(board, player)
    else:
        raise Exception("Invalid Player : " + player_type)
def print_game_info():
    print('''
Welcome to Tic Tac Toe.
Player 1 is 'O'
Player 2 is 'X' 
    ''')
def Game(player_types):
    print_game_info()
    # Starting Game
    print("Initializing Board")
    board = new_board()
    players = ['O','X']
    chance = 0
    while True:
        player = players[chance%2]
        player_type = player_types[chance%2]
        render(board)
        move_coords = get_player_move(player_type, player, board)
        board = make_move(board, move_coords, player)
        winner = get_winner(board)
        if winner is not None:
            render(board)
            print("\nWohoo {} has Won!!!\nRun Again\n".format(winner))
            break
        if is_board_full(board):
            render(board)
            print("\nOhho! This is a draw. Begin Again\n")
            break
        chance+=1

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        raise Exception("Please Specify player_types example: 'tictactoe.py human random_ai'")
    Game(sys.argv[1:])

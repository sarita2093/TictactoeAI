import random
import utils

def random_ai(board, player):
    is_valid_move = False;
    while is_valid_move is False:
        move =  (random.randint(0, 2),random.randint(0, 2))
        is_valid_move = utils.is_a_valid_move(board, move)
    return move

'''
function that returns a winning move if one exists, and a random move otherwise
Test : 

board = [
  ['X', 'O', None],
  [None, 'O', None],
  ['X', None, None]
]
print finds_winning_moves_ai(board, 'X')
print finds_winning_moves_ai(board, 'X')
# => should always print (1, 0)

print finds_winning_moves_ai(board, 'O')
print finds_winning_moves_ai(board, 'O')
# => should always print (2, 1)

'''
def finds_winning_moves_ai(board, player):
    winning_move = None
    for i in range(0,3):
        for j in range(0,3):
            move = (i,j)
            if(utils.is_a_valid_move(board,move)):
                temp_board = utils.make_move(board, move, player)
                if utils.get_winner(temp_board) is player:
                    # This is a winning move.  
                    winning_move = move
                    break   
    return winning_move if winning_move is not None else random_ai(board, player)
'''
finds_winning_and_losing_moves_ai should return, in order of preference: a move that wins, a move that block a loss, and a random move.
Test:
board = [
  ['X', 'O', None],
  [None, 'O', None],
  ['X', None, None]
]
print finds_winning_moves_ai(board, 'X')
print finds_winning_moves_ai(board, 'X')
# => should always print (1, 0)


board = [
  ['X', 'O', None],
  [None, 'O', None],
  ['O', None, 'X']
]
utils.render(board)
print finds_winning_and_losing_moves_ai(board, 'X')
print finds_winning_and_losing_moves_ai(board, 'X')
# => should always print (2, 1)

'''
def finds_winning_and_losing_moves_ai(board, player):
    # Checking if we can win
    supposed_winning_move =  finds_winning_moves_ai(board,player)
    temp_board =  utils.make_move(board, supposed_winning_move, player)
    if utils.get_winner(temp_board) is player:
        return supposed_winning_move
    # Checking if we can loose
    opposite_player = utils.get_opposite_player(player)
    supposed_opposite_winning_move = finds_winning_moves_ai(board,opposite_player)
    temp_board =  utils.make_move(board, supposed_opposite_winning_move, opposite_player)
    if utils.get_winner(temp_board) is opposite_player:
        return supposed_opposite_winning_move # block this move so opponent cannot play this. 

    return random_ai(board, player)
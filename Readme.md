## Tictactoe AI
I like games. Since childhoold video games have always fascinated me. I always wondered, if it would be nice to have my own game. I think this is the first of many. I like tic tac toe, it's simple but i enjoy it. 
I wanted to play against a computer so i decided to keep some AI.
### To Play game
```shell
git clone https://github.com/sarita2093/TictactoeAI.git

# Supply 2 agents, obth agents could be human|random_ai|winning_ai

python tictactoe.py human random_ai

#or play with your friend

python tictactoe.py human human

```

### Ai functions
I made few basic AI functions, You can also make your own functions and see if yours beat mine ;)
The interface is simple. Define your ai and add it to ai.py and refrence in tictactoe.py -> get_player_move method. 
```python
'''
board is a list of lists. Example - [['X','O',None],[None,None,None],[None,None,None]]. It represents current board. 
player is 'X' or 'O'
move is a tuple (x,y) coordinates, representing move your ai would make. 
'''
def your_ai(board, player):
    # Your Logic
    return move

```

### Todo
- Add Minimax Algorithm based AI
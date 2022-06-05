"""
Tic Tac Toe Player
"""

from cmath import inf
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount=0
    Ocount=0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                Xcount += 1
            elif board[i][j] == O:
                Ocount += 1

    if Xcount > Ocount:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    availablemoves=set()
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                availablemoves.add((i, j))

    return availablemoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==X and board[0][1]==X and board[0][2]==X:
        return X
    elif board[1][0]==X and board[1][1]==X and board[1][2]==X: 
        return X
    elif board[2][0]==X and board[2][1]==X and board[2][2]==X: 
        return X
    elif board[0][0]==X and board[1][0]==X and board[2][0]==X: 
        return X
    elif board[0][1]==X and board[1][1]==X and board[2][1]==X: 
        return X
    elif board[0][2]==X and board[1][2]==X and board[2][2]==X: 
        return X
    elif board[0][0]==X and board[1][1]==X and board[2][2]==X: 
        return X
    elif board[0][2]==X and board[1][1]==X and board[2][0]==X: 
        return X
    elif board[0][0]==O and board[0][1]==O and board[0][2]==O:
        return O
    elif board[1][0]==O and board[1][1]==O and board[1][2]==O: 
        return O
    elif board[2][0]==O and board[2][1]==O and board[2][2]==O: 
        return O 
    elif board[0][0]==O and board[1][0]==O and board[2][0]==O: 
        return O
    elif board[0][1]==O and board[1][1]==O and board[2][1]==O: 
        return O 
    elif board[0][2]==O and board[1][2]==O and board[2][2]==O: 
        return O
    elif board[0][0]==O and board[1][1]==O and board[2][2]==O: 
        return O
    elif board[0][2]==O and board[1][1]==O and board[2][0]==O: 
        return O
    else:
        return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v =float("-inf")
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v =float("inf")
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move
        
    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
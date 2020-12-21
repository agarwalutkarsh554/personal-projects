import math
from itertools import cycle
import copy

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
    count_x = 0

    count_o = 0



    for i in range(3):

        for j in range(3):

            if(board[i][j] ==  "X"):

                count_x +=1

            elif(board[i][j] ==  "O"):

                count_o +=1



    if(count_o < count_x):

        return O

    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    if terminal(board):
        pass
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)

    return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    count_x_row = 0

    count_o_row = 0

    count_x_col = 0

    count_o_col = 0

    count_x_diag = 0

    count_o_diag = 0

    count_x_diag_1 = 0

    count_o_diag_1 = 0

    for i in range(3):

        for j in range(3):

            if (board[i][j] == X):

                count_x_row += 1

            elif (board[i][j] == O):

                count_o_row += 1

            if (board[j][i] == X):

                count_x_col += 1

            elif (board[j][i] == O):

                count_o_col += 1

            if (i == j and board[i][j] == X):

                count_x_diag += 1

            elif (i == j and board[i][j] == O):

                count_o_diag += 1

            if (i + j == 2 and board[i][j] == X):

                count_x_diag_1 += 1

            elif (i + j == 2 and board[i][j] == O):

                count_o_diag_1 += 1

        if (count_o_row == 3 or count_o_col == 3):

            return O

        elif (count_x_row == 3 or count_x_col == 3):

            return X


        count_x_row = 0

        count_x_col = 0

        count_o_row = 0

        count_o_col = 0

    if (count_o_diag == 3 or count_o_diag_1 == 3):

        return O

    elif (count_x_diag == 3 or count_x_diag_1 == 3):

        return X

    else:

        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    p = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                p = 1
                break

    if winner(board) == X or winner(board) == O:
        return True
    elif winner(board) == EMPTY:
        if p == 0:
            return True
        elif p == 1:
            p = 0
            return False



def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    p = player(board)



    if(p==X):

        value = float("-inf")

        action_select = None



        for action in actions(board):

            minValueResult = minValue(result(board, action))



            if minValueResult > value:

                value = minValueResult

                action_select = action



    elif(p==O):


        value = float("inf")

        action_select = None



        for action in actions(board):

            maxValueResult = maxValue(result(board, action))



            if maxValueResult < value:

                value = maxValueResult

                action_select = action



    return action_select




def maxValue(board):

    if terminal(board):

        return utility(board)

    v = float('-inf')

    for action in actions(board):

        v = max(v,minValue(result(board, action)))

    return v


def minValue(board):

    if terminal(board):

        return utility(board)

    v = float('inf')

    for action in actions(board):

        v = min(v,maxValue(result(board, action)))

    return v

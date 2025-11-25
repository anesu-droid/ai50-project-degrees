import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    if x_count <= o_count:
        return X
    else:
        return O

def actions(board):
    if terminal(board):
        return set()
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves

def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for row in board:
        if row == [X, X, X]:
            return X
        if row == [O, O, O]:
            return O
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]]
        if column == [X, X, X]:
            return X
        if column == [O, O, O]:
            return O
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    if diag1 == [X, X, X] or diag2 == [X, X, X]:
        return X
    if diag1 == [O, O, O] or diag2 == [O, O, O]:
        return O
    return None

def terminal(board):
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    current = player(board)
    if current == X:
        best_value = -math.inf
        best_move = None
        for move in actions(board):
            value = min_value(result(board, move))
            if value > best_value:
                best_value = value
                best_move = move
        return best_move
    else:
        best_value = math.inf
        best_move = None
        for move in actions(board):
            value = max_value(result(board, move))
            if value < best_value:
                best_value = value
                best_move = move
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v

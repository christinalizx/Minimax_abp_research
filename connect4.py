import math
import copy


def get_child_boards(player, board):
    """
    Generate a list of successor boards obtained by placing a checker for a given player

    Parameters
    ----------
    player: board.PLAYER1 or board.PLAYER2
        the player who will place a checker in the board
    board: the current board instance
    Returns
    -------
    a list of (col, new_board) tuples,
    where col is the column in which a new checker is placed and
    is counted from the left column as 0, and
    new_board is the resulting board instance
    """
    res = []
    for c in range(board.cols):
        if board.placeable(c):
            tmp_board = board.clone()
            tmp_board.place(player, c)
            res.append((c, tmp_board))
    return res


def evaluate(player, board):
    """

    Parameters
    ----------
    player : The player from the board instance
    board : The board instance

    Returns
    -------
    value: the score

    """
    adversary = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    score = [0] * 5
    adv_score = [0] * 5
    weights = [0, 1, 4, 16, 1000]

    # Obtain all 4-slot segments on the board
    seg = []
    invalid_slot = -1
    left_revolved = [
        [invalid_slot] * r + board.row(r) + \
        [invalid_slot] * (board.rows - 1 - r) for r in range(board.rows)
    ]
    right_revolved = [
        [invalid_slot] * (board.rows - 1 - r) + board.row(r) + \
        [invalid_slot] * r for r in range(board.rows)
    ]
    for r in range(board.rows):
        # row
        row = board.row(r)
        for c in range(board.cols - 3):
            seg.append(row[c:c + 4])
    for c in range(board.cols):
        # col
        col = board.col(c)
        for r in range(board.rows - 3):
            seg.append(col[r:r + 4])
    for c in zip(*left_revolved):
        # slash
        for r in range(board.rows - 3):
            seg.append(c[r:r + 4])
    for c in zip(*right_revolved):
        # backslash
        for r in range(board.rows - 3):
            seg.append(c[r:r + 4])
    # compute score
    for s in seg:
        if invalid_slot in s:
            continue
        if adversary not in s:
            score[s.count(player)] += 1
        if player not in s:
            adv_score[s.count(adversary)] += 1
    reward = sum([s * w for s, w in zip(score, weights)])
    penalty = sum([s * w for s, w in zip(adv_score, weights)])
    value = reward - penalty
    return value


def minimax(player, board, depth_limit, maxing_player=True):
    """

    Parameters
    ----------
    player : The player from the board instance
    board : The board instance
    depth_limit : int, the maximum depth the algorithm can reach
    maxing_player : boolean to show if the current player is maximizing or minimizing player

    Returns
    -------
    placement: int, the current column
    score: float, the current score

    """
    adversary = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    placement = None

    if depth_limit == 0 or board.terminal():
        if maxing_player == True:
            score = evaluate(player, board)
        else:
            score = evaluate(adversary, board)
    else:
        if maxing_player == True:
            score = -math.inf
            for col in range(board.cols):
                if board.placeable(col):
                    new_board = copy.deepcopy(board)
                    new_board.place(player, col)
                    current_placement, current_score = minimax(adversary, new_board, depth_limit - 1,
                                                               maxing_player=False)
                    if current_score > score:
                        score = current_score
                        placement = col

        else:
            score = math.inf
            for col in range(board.cols):
                if board.placeable(col):
                    new_board = copy.deepcopy(board)
                    new_board.place(player, col)
                    current_placement, current_score = minimax(adversary, new_board, depth_limit - 1,
                                                               maxing_player=True)
                    if current_score < score:
                        score = current_score
                        placement = col
    return placement, score


def alphabeta(player, board, depth_limit, alpha=-math.inf, beta=math.inf, maxing_player=True):
    """

    Parameters
    ----------
    player : The player from the board instance
    board : The board instance
    depth_limit : int, the maximum depth the algorithm can reach
    alpha: float, negative infinity
    beta: float, positive infinity
    maxing_player : boolean, to show if the current player is maximizing or minimizing player

    Returns
    -------
    placement: int, the current column
    score: float, the current score

    """
    adversary = board.PLAYER2 if player == board.PLAYER1 else board.PLAYER1
    placement = None

    if depth_limit == 0 or board.terminal():
        if maxing_player == True:
            score = evaluate(player, board)
        else:
            score = evaluate(adversary, board)

    else:
        if maxing_player == True:
            score = float("-inf")
            x = get_child_boards(player, board)
            for i in x:
                col, new_board = i
                current_placement, current_score = alphabeta(adversary, new_board, depth_limit - 1, alpha, beta,
                                                             maxing_player=False)
                if current_score > score:
                    score = current_score
                    placement = col
                alpha = max(score, alpha)
                if alpha >= beta:
                    break


        else:
            score = float("+inf")
            x = get_child_boards(player, board)
            for i in x:
                col, new_board = i
                current_placement, current_score = alphabeta(adversary, new_board, depth_limit - 1, alpha, beta,
                                                             maxing_player=True)
                if current_score < score:
                    score = current_score
                    placement = col
                beta = min(score, beta)
                if alpha >= beta:
                    break
    return placement, score


if __name__ == "__main__":
    from utils.app import App, Board
    import tkinter

    algs = {
        "Minimax": minimax,
        "Alpha-beta pruning": alphabeta,
    }

    root = tkinter.Tk()
    App(algs, root)
    root.mainloop()

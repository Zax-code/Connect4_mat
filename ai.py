def IAplay(board, depth):
    best = float("-inf")
    bestMove = -1
    iaSymbol = board.turn
    for i in range(board.col):
        if board.play(i):
            move = minmax(board, depth, iaSymbol)
            board.undo(i)
            if move > best:
                best = move
                bestMove = i
    board.play(bestMove)
    return bestMove


def minmax(board, depth, aiSymbol):
    if board.winner == aiSymbol:
        return float("inf")
    elif board.winner and board.winner != aiSymbol:
        return float("-inf")
    elif depth == 0 or board.chips == 0:
        return heuristic(board, aiSymbol)
    if board.turn == aiSymbol:
        best = float("-inf")
        for i in range(board.col):
            if board.play(i):
                best = max(best, minmax(board, depth-1, aiSymbol))
                board.undo(i)
        return best
    else:
        best = float("inf")
        for i in range(board.col):
            if board.play(i):
                best = min(best, minmax(board, depth-1, aiSymbol))
                board.undo(i)
        return best


def heuristic(board, aiSymbol):
    multiplier = [1, 5]
    score = countVertical(board, aiSymbol, multiplier) + \
        countHorizontal(board, aiSymbol, multiplier) + \
        countDiagonal(board, aiSymbol, multiplier)
    return score


def countVertical(board, aiSymbol, multiplier):
    inARow = 0
    threes = 0
    twos = 0
    for i in range(board.col):
        for j in range(board.row):
            if board.board[j][i] == aiSymbol:
                inARow += 1
            else:
                inARow = 0
            if inARow == 3:
                threes += 1
                twos -= 1
            elif inARow == 2:
                twos += 1
        inARow = 0
    return twos * multiplier[0] + threes * multiplier[1]


def countHorizontal(board, aiSymbol, multiplier):
    inARow = 0
    threes = 0
    twos = 0
    for i in range(board.row):
        for j in range(board.col):
            if board.board[i][j] == aiSymbol:
                inARow += 1
            else:
                inARow = 0
            if inARow == 3:
                threes += 1
                twos -= 1
            elif inARow == 2:
                twos += 1
        inARow = 0
    return twos * multiplier[0] + threes * multiplier[1]


def countDiagonal(board, aiSymbol, multiplier):
    inARow = [0, 0, 0, 0]
    threes = 0
    twos = 0
    for i in range(board.row-1):
        for j in range(board.row):
            if j+i < board.row:
                if board.board[j+i][j] == aiSymbol:
                    inARow[0] += 1
                else:
                    inARow[0] = 0
                if board.board[j+i][board.col - 1 - j] == aiSymbol:
                    inARow[2] += 1
                else:
                    inARow[2] = 0
            if j+i < board.col:
                if board.board[j][j+i] == aiSymbol:
                    inARow[1] += 1
                else:
                    inARow[1] = 0
                if board.board[j][board.col - 1 - j-i] == aiSymbol:
                    inARow[3] += 1
                else:
                    inARow[3] = 0
            for r in inARow:
                if r == 3:
                    threes += 1
                    twos -= 1
                elif r == 2:
                    twos += 1
        inARow = [0, 0, 0, 0]

    return twos * multiplier[0] + threes * multiplier[1]

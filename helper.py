#
def GenerateBlackMovesOpening(board):
    swapped_board = swapColors(board)

    result = []

    for state in GenerateAdd(swapped_board):
        result.append(swapColors(state))

    return result


#
def GenerateBlackMovesMidgameEndgame(board):
    swapped_board = swapColors(board)

    if board.count("B") == 3:
        lst = GenerateHopping(swapped_board)
    else:
        lst = GenerateMove(swapped_board)

    result = []

    for state in lst:
        result.append(swapColors(state))

    return result


#
def GenerateMovesOpening(board):
    return GenerateAdd(board)


#
def GenerateMovesMidgameEndgame(board):
    if board.count("W") == 3:
        return GenerateHopping(board)
    else:
        return GenerateMove(board)


#
def GenerateAdd(board):
    L = []
    for i in range(len(board)):
        if board[i] == "x":
            b = board[::]
            b = list(b)
            b[i] = "W"
            b = "".join(b)

            if closeMill(i, b):
                L = GenerateRemove(b, L)
            else:
                L.append(b)

    return L


#
def GenerateHopping(board):
    # print("hopped")
    L = []

    for i in range(len(board)):
        if board[i] == "W":
            for j in range(len(board)):
                if board[j] == "x":
                    b = board[::]
                    b = list(b)
                    b[i] = "x"
                    b[j] = "W"
                    b = "".join(b)

                    if closeMill(j, b):
                        L = GenerateRemove(b, L)
                    else:
                        L.append(b)

    return L


#
def GenerateMove(board):
    L = []

    for i in range(len(board)):
        if board[i] == "W":
            n = neighbors(i)

            for nei in n:
                if board[nei] == "x":
                    b = list(board[::])
                    b[i] = "x"
                    b[nei] = "W"
                    b = "".join(b)

                    if closeMill(nei, b):
                        L = GenerateRemove(b, L)
                    else:
                        L.append(b)

    return L


#
def GenerateRemove(board, L):
    found = False

    for i in range(len(board)):
        if board[i] == "B" and (not closeMill(i, board)):
            found = True

            b = board[::]
            b = list(b)
            b[i] = "x"
            b = "".join(b)
            L.append(b)

    if not found:
        L.append(board)

    return L


#
def neighbors(j):
    match j:
        case 0:
            return [1, 3, 19]
        case 1:
            return [0, 4, 2]
        case 2:
            return [1, 5, 12]
        case 3:
            return [0, 6, 8, 4]
        case 4:
            return [1, 3, 5]
        case 5:
            return [7, 4, 2, 11]
        case 6:
            return [9, 7, 3]
        case 7:
            return [10, 6, 5]
        case 8:
            return [3, 16, 9]
        case 9:
            return [13, 6, 8]
        case 10:
            return [15, 11, 7]
        case 11:
            return [10, 12, 18, 5]
        case 12:
            return [2, 11, 21]
        case 13:
            return [16, 9, 14]
        case 14:
            return [17, 13, 15]
        case 15:
            return [14, 10, 18]
        case 16:
            return [19, 8, 13, 17]
        case 17:
            return [20, 16, 18, 14]
        case 18:
            return [21, 15, 17, 11]
        case 19:
            return [0, 20, 16]
        case 20:
            return [19, 17, 21]
        case 21:
            return [20, 12, 18]


#
def closeMill(j, board):
    C = board[j]

    match j:
        case 0:
            if (board[1] == C and board[2] == C) or (board[3] == C and board[6] == C):
                return True
        case 1:
            if board[0] == C and board[2] == C:
                return True
        case 2:
            if (board[0] == C and board[1] == C) or (board[12] == C and board[21] == C) or \
                    (board[5] == C and board[7] == C):
                return True
        case 3:
            if (board[0] == C and board[6] == C) or (board[4] == C and board[5] == C) or \
                    (board[8] == C and board[16] == C):
                return True
        case 4:
            if board[3] == C and board[5] == C:
                return True
        case 5:
            if (board[3] == C and board[4] == C) or (board[11] == C and board[18] == C) or \
                    (board[2] == C and board[7] == C):
                return True
        case 6:
            if (board[0] == C and board[3] == C) or (board[9] == C and board[13] == C):
                return True
        case 7:
            if (board[2] == C and board[5] == C) or (board[10] == C and board[15] == C):
                return True
        case 8:
            if board[3] == C and board[16] == C:
                return True
        case 9:
            if board[6] == C and board[13] == C:
                return True
        case 10:
            if (board[11] == C and board[12] == C) or (board[7] == C and board[15] == C):
                return True
        case 11:
            if (board[10] == C and board[12] == C) or (board[5] == C and board[18] == C):
                return True
        case 12:
            if (board[10] == C and board[11] == C) or (board[2] == C and board[21] == C):
                return True
        case 13:
            if (board[16] == C and board[19] == C) or (board[14] == C and board[15] == C) or \
                    (board[6] == C and board[9] == C):
                return True
        case 14:
            if (board[13] == C and board[15] == C) or (board[17] == C and board[20] == C):
                return True
        case 15:
            if (board[13] == C and board[14] == C) or (board[7] == C and board[10] == C) or \
                    (board[18] == C and board[21] == C):
                return True
        case 16:
            if (board[17] == C and board[18] == C) or (board[13] == C and board[19] == C) or \
                    (board[3] == C and board[8] == C):
                return True
        case 17:
            if (board[16] == C and board[18] == C) or (board[14] == C and board[20] == C):
                return True
        case 18:
            if (board[16] == C and board[17] == C) or (board[5] == C and board[11] == C) or \
                    (board[15] == C and board[21] == C):
                return True
        case 19:
            if (board[13] == C and board[16] == C) or (board[20] == C and board[21] == C):
                return True
        case 20:
            if (board[19] == C and board[21] == C) or (board[14] == C and board[17] == C):
                return True
        case 21:
            if (board[19] == C and board[20] == C) or (board[15] == C and board[18] == C) or \
                    (board[2] == C and board[12] == C):
                return True

        case _:
            return False


def staticEstimationOpening(board):
    numWhitePieces = board.count("W")
    numBlackPieces = board.count("B")

    return numWhitePieces - numBlackPieces


def staticEstimationMidGameEndGame(board):
    numWhitePieces = board.count("W")
    numBlackPieces = board.count("B")
    numBlackMoves = len(GenerateBlackMovesMidgameEndgame(board))

    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000

    else:
        return 10000 * (numWhitePieces - numBlackPieces) - numBlackMoves


#
def swapColors(board):
    board = board.replace("W", "Z")
    board = board.replace("B", "W")
    board = board.replace("Z", "B")

    return board


def staticEstimationOpeningImproved(board):
    numWhitePieces = board.count("W")
    numBlackPieces = board.count("B")
    numBlackMoves = len(GenerateBlackMovesMidgameEndgame(board))
    numWhiteMoves = len(GenerateMovesMidgameEndgame(board))

    return 1000 * (numWhitePieces - numBlackPieces) + numWhiteMoves - numBlackMoves


def staticEstimationMidGameEndGameImproved(board):
    numWhitePieces = board.count("W")
    numBlackPieces = board.count("B")
    numBlackMoves = len(GenerateBlackMovesMidgameEndgame(board))
    numWhiteMoves = len(GenerateMovesMidgameEndgame(board))

    closedMills = 0

    for i in range(len(board)):
        if closeMill(i, board):
            closedMills += 1

    if numBlackPieces <= 2:
        return 10000
    elif numWhitePieces <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000
    else:
        return 1000 * (numWhitePieces - numBlackPieces) + closedMills + numWhiteMoves - numBlackMoves

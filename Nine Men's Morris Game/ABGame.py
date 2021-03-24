import sys
import GameMove

maxValue = float('inf')
minValue = float('-inf')



def ABGame(depth, currBoard, alpha, beta, playerW):
    result = GameMove.evaluator()
    if depth == 0:
        numWhitePieces = 0
        numBlackPieces = 0
        for pos in range(len(currBoard)):
            if currBoard[pos] == 'W':
                numWhitePieces += 1
            elif currBoard[pos] == 'B':
                numBlackPieces += 1
        L = GameMove.generateMovesMidgameEndgameBlack(currBoard)
        numBlackMoves = len(L)
        if numBlackPieces <= 2: result.value = 10000
        elif numWhitePieces <= 2: result.value = -10000
        elif numBlackMoves == 0: result.value = 10000
        else:
            result.value = 1000 * (numWhitePieces - numBlackPieces) - numBlackMoves
        result.count += 1
        return result
    if playerW:
        possibleMoves = GameMove.generateMovesMidgameEndgame(currBoard)

    else:
        possibleMoves = GameMove.generateMovesMidgameEndgameBlack(currBoard)

    for b in possibleMoves:
        if playerW:
            check = ABGame(depth - 1, b, alpha, beta, False)
            if check.value > alpha:
                alpha = check.value
                result.board = b
            result.count += check.count
        else:
            check = ABGame(depth - 1, b, alpha, beta, True)
            if check.value < beta:
                beta = check.value
                result.board = b
            result.count += check.count
        if alpha >= beta:
            break

    if playerW: result.value = alpha
    else: result.value = beta
    return result

if __name__ == '__main__':

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w")
    depth = int(sys.argv[3])
    input_board=list(file1.read())
    output_board=''
    result = ABGame(depth, input_board, minValue,maxValue,True)
    for char in result.board:
        output_board += char
    file2.write(output_board)
    print("Board Position:", output_board)
    print("Position evaluated by static estimation:",result.count)
    print("AB Esitmate:",result.value)

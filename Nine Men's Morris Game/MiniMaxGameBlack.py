import sys
import GameMove

maxValue = float('inf')
minValue = float('-inf')


def MiniMaxGameBlack(depth, currBoard, playerW):
    result = GameMove.evaluator()
    if depth == 0:
        numWhitePieces= 0
        numBlackPieces = 0
        for pos in range(len(currBoard)):
            if currBoard[pos] == 'W':
                numWhitePieces += 1
            elif currBoard[pos] == 'B':
                numBlackPieces += 1
        L = GameMove.generateMovesMidgameEndgame(currBoard)
        numWhiteMoves = len(L)
        if numBlackPieces <= 2: result.value = 10000
        elif numWhitePieces <= 2: result.value = -10000
        elif numWhiteMoves == 0: result.value = 10000
        else:
            result.value = 1000 * (numBlackPieces-numWhitePieces) - numWhiteMoves
        result.count += 1
        return result

    if playerW:
        possibleMoves = GameMove.generateMovesMidgameEndgame(currBoard)
        result.value = maxValue
    else:
        possibleMoves  = GameMove.generateMovesMidgameEndgameBlack(currBoard)
        result.value = minValue

    for b in possibleMoves:
        if playerW:
            check = MiniMaxGameBlack(depth - 1, b, False)
            if check.value < result.value:
                result.value = check.value
                result.board = b
            result.count += check.count

        else:
            check = MiniMaxGameBlack(depth - 1, b, True)
            if check.value > result.value:
                result.value = check.value
                result.board = b
            result.count += check.count
    return result

if __name__ == '__main__':

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w")
    depth = int(sys.argv[3])
    input_board=list(file1.read())
    output_board=''
    result = MiniMaxGameBlack(depth, input_board, False)
    for char in result.board:
        output_board += char
    file2.write(output_board)
    print("Board Position:", output_board)
    print("Position evaluated by static estimation:",result.count)
    print("MINIMAX esitmate:",result.value)



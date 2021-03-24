import sys
import GameMove

maxValue = float('inf')
minValue = float('-inf')



def ABOpening(depth, currBoard, alpha, beta, playerW):
    result = GameMove.evaluator()
    if depth == 0:
        openCount = GameMove.staticEstimateOpening(currBoard)
        result.value = openCount
        result.count +=1
        return result

    if playerW:
        newBoard = GameMove.generateMoveOpening(currBoard)
    else:
        newBoard = GameMove.generateMoveOpeningBlack(currBoard)

    for position in newBoard:
        if playerW:
            check = ABOpening(depth - 1, position, alpha, beta, False)
            if check.value > alpha:
                alpha = check.value
                result.board = position
            result.count += check.count
        else:
            check = ABOpening(depth - 1, position, alpha, beta, True)
            if check.value < beta:
                beta = check.value
                check.board = position
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
    result = ABOpening(depth, input_board, minValue,maxValue,True)
    for char in result.board:
        output_board += char
    file2.write(output_board)
    print("Board Position:", output_board)
    print("Position evaluated by static estimation:",result.count)
    print("AB Esitmate:",result.value)

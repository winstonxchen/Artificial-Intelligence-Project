import sys
import GameMove

maxValue = float('inf')
minValue = float('-inf')

def MiniMaxImproved(depth, currBoard, playerW):
    result = GameMove.evaluator()
    if depth == 0:
        openCount = GameMove.staticEstimateOpeningImproved(currBoard)
        result = GameMove.evaluator(openCount, result.count + 1, currBoard)
        return result
    if playerW:
        newBoard= GameMove.generateMoveOpening(currBoard)
        result.value = minValue
    else:
        newBoard = GameMove.generateMoveOpeningBlack(currBoard)
        result.value = maxValue
    for position in newBoard:
        if playerW:
            check = MiniMaxImproved(depth - 1,position, False)
            if check.value > result.value:
                result.value = check.value
                result.board = position
            result.count += check.count
        else:
            check = MiniMaxImproved(depth - 1, position, True)
            if check.value < result.value:
                result.value = check.value
                result.board = position
            result.count += check.count
    return result

if __name__ == '__main__':

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w")
    depth = int(sys.argv[3])
    input_board=list(file1.read())
    output_board=''
    result = MiniMaxImproved(depth, input_board, True)
    for char in result.board:
        output_board += char
    file2.write(output_board)
    print("Board Position:", output_board)
    print("Position evaluated by static estimation:",result.count)
    print("MINIMAX esitmate:",result.value)



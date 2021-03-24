from copy import deepcopy

class evaluator(object):
    count = 0
    value = 0
    board = []

    def __init__(self, value=0, count=0, board=[]):
        self.count = count
        self.value = value
        self.board = board

def checkMill(position, b):
    C = b[position]
    if (C == 'x'):
        return False
    elif (position == 0):
        if ((b[1] == C and b[2] == C) or (b[3] == C and b[6] == C) or (b[8] == C and b[20] == C)): return True
        return False
    elif (position == 1):
        if (b[0] == C and b[2] == C):return True
        return False
    elif (position == 2):
        if ((b[0] == C and b[1] == C) or (b[5] == C and b[7] == C) or (b[13] == C and b[22] == C)):return True
        return False
    elif (position == 3):
        if ((b[0] == C and b[6] == C) or (b[4] == C and b[5] == C) or (b[9] == C and b[17] == C)):return True
        return False
    elif (position == 4):
        if (b[3] == C and b[5] == C):return True
        return False
    elif (position == 5):
        if ((b[3] == C and b[4] == C) or (b[2] == C and b[7] == C) or (b[12] == C and b[19] == C)):return True
        return False
    elif (position == 6):
        if ((b[0] == C and b[3] == C) or (b[10] == C and b[14] == C)):return True
        return False
    elif (position == 7):
        if ((b[2] == C and b[5] == C) or (b[11] == C and b[16] == C)):return True
        return False
    elif (position == 8):
        if ((b[0] == C and b[20] == C) or (b[9] == C and b[10] == C)):return True
        return False
    elif (position == 9):
        if ((b[8] == C and b[10] == C) or (b[3] == C and b[17] == C)):return True
        return False
    elif (position == 10):
        if ((b[8] == C and b[9] == C) or (b[6] == C and b[14] == C)):return True
        return False
    elif (position == 11):
        if ((b[7] == C and b[16] == C) or (b[12] == C and b[13] == C)):return True
        return False
    elif (position == 12):
        if ((b[11] == C and b[13] == C) or (b[5] == C and b[19] == C)):return True
        return False
    elif (position == 13):
        if ((b[11] == C and b[12] == C) or (b[2] == C and b[22] == C)):return True
        return False
    elif (position == 14):
        if ((b[17] == C and b[20] == C) or (b[15] == C and b[16] == C) or (b[6] == C and b[10] == C)):return True
        return False
    elif (position == 15):
        if ((b[14] == C and b[16] == C) or (b[18] == C and b[21] == C)):return True
        return False
    elif (position == 16):
        if ((b[14] == C and b[15] == C) or (b[19] == C and b[22] == C) or (b[7] == C and b[11] == C)):return True
        return False
    elif (position == 17):
        if ((b[3] == C and b[9] == C) or (b[14] == C and b[20] == C) or (b[18] == C and b[19] == C)):return True
        return False
    elif (position == 18):
        if ((b[17] == C and b[19] == C) or (b[15] == C and b[21] == C)):return True
        return False
    elif (position == 19):
        if ((b[17] == C and b[18] == C) or (b[16] == C and b[22] == C) or (b[5] == C and b[12] == C)):return True
        return False
    elif (position == 20):
        if ((b[0] == C and b[8] == C) or (b[14] == C and b[17] == C) or (b[21] == C and b[22] == C)):return True
        return False
    elif (position == 21):
        if ((b[20] == C and b[22] == C) or (b[15] == C and b[18] == C)):return True
        return False
    elif (position == 22):
        if ((b[2] == C and b[13] == C) or (b[16] == C and b[19] == C) or (b[20] == C and b[21] == C)):return True
        return False
    else:
        return False

def neighbors(position):
    neighborList = []
    if position == 0:
        neighborList.append(1)
        neighborList.append(3)
        neighborList.append(8)
    elif position == 1:
        neighborList.append(0)
        neighborList.append(2)
        neighborList.append(4)
    elif position == 2:
        neighborList.append(1)
        neighborList.append(5)
        neighborList.append(13)
    elif position == 3:
        neighborList.append(0)
        neighborList.append(4)
        neighborList.append(6)
        neighborList.append(9)
    elif position == 4:
        neighborList.append(1)
        neighborList.append(3)
        neighborList.append(5)
    elif position == 5:
        neighborList.append(2)
        neighborList.append(4)
        neighborList.append(7)
        neighborList.append(12)
    elif position == 6:
        neighborList.append(3)
        neighborList.append(7)
        neighborList.append(10)
    elif position == 7:
        neighborList.append(5)
        neighborList.append(6)
        neighborList.append(11)
    elif position == 8:
        neighborList.append(0)
        neighborList.append(9)
        neighborList.append(20)
    elif position == 9:
        neighborList.append(3)
        neighborList.append(8)
        neighborList.append(10)
        neighborList.append(17)
    elif position == 10:
        neighborList.append(6)
        neighborList.append(9)
        neighborList.append(14)
    elif position == 11:
        neighborList.append(7)
        neighborList.append(12)
        neighborList.append(16)
    elif position == 12:
        neighborList.append(5)
        neighborList.append(11)
        neighborList.append(13)
        neighborList.append(19)
    elif position == 13:
        neighborList.append(2)
        neighborList.append(12)
        neighborList.append(22)
    elif position == 14:
        neighborList.append(10)
        neighborList.append(15)
        neighborList.append(17)
    elif position == 15:
        neighborList.append(14)
        neighborList.append(16)
        neighborList.append(18)
    elif position == 16:
        neighborList.append(11)
        neighborList.append(15)
        neighborList.append(19)
    elif position == 17:
        neighborList.append(9)
        neighborList.append(14)
        neighborList.append(18)
        neighborList.append(20)
    elif position == 18:
        neighborList.append(15)
        neighborList.append(17)
        neighborList.append(19)
        neighborList.append(21)
    elif position == 19:
        neighborList.append(12)
        neighborList.append(16)
        neighborList.append(18)
        neighborList.append(22)
    elif position == 20:
        neighborList.append(8)
        neighborList.append(17)
        neighborList.append(21)
    elif position == 21:
        neighborList.append(18)
        neighborList.append(20)
        neighborList.append(22)
    elif position == 22:
        neighborList.append(13)
        neighborList.append(19)
        neighborList.append(21)
    else:
        return neighborList
    return neighborList

def staticEstimateOpening(b):
    numWhitePieces = 0
    numBlackPiece = 0
    for pos in range(len(b)):
        if (b[pos] == 'W'):
            numWhitePieces +=1
        elif (b[pos] == 'B'):
            numBlackPiece +=1
        else:
            continue
    return numWhitePieces-numBlackPiece


def reverse(board):
    flippedBoard=[]
    for pos in range(len(board)):
        check = board[pos]
        if check == 'B':
            flippedBoard.append('W')
        elif check == 'W':
            flippedBoard.append('B')
        else:
            flippedBoard.append('x')
    return flippedBoard



def generateMoveOpening(bPosition):
    newB = generateAdd(bPosition)
    return newB

# Adding new white piece
def generateAdd(bPosition):
    L=[]
    for pos in range(len(bPosition)):
        if bPosition[pos] == 'x':
            b = deepcopy(bPosition)
            b[pos] = 'W'
            if checkMill(pos, b):
                L = generateRemove(b, L)
            else:
                L.append(b)
    return L


def generateMoveOpeningBlack(bPosition):
    tempb = reverse(bPosition)
    blackMoves = generateAdd(tempb)
    moves = []
    for each in range(len(blackMoves)):
        b = blackMoves[each]
        moves.insert(each, reverse(b))
    return moves

def generateRemove(bPosition, L):
    for pos in range(len(bPosition)):
        if bPosition[pos] == 'B':
            if checkMill(pos, bPosition) == False:
                newB = deepcopy(bPosition)
                newB[pos] = 'x'
                L.append(newB)
    return L

def generateMovesMidgameEndgame(bPosition):
    numWhitePiece = 0
    for position in range(len(bPosition)):
        if bPosition[position] == 'W':
            numWhitePiece += 1
    if numWhitePiece == 3:
        L = generateHopping(bPosition)
    else:
        L = generateMove(bPosition)
    return L

def generateMove(bPosition):
    L=[]
    for location in range(len(bPosition)):
        if bPosition[location] == 'W':
            n = neighbors(location)
            for neighbor in n:
                if bPosition[neighbor] == 'x':
                    copy_b = deepcopy(bPosition)
                    copy_b[location] = 'x'
                    copy_b[neighbor] = 'W'
                    if checkMill(neighbor, copy_b):
                        L = generateRemove(copy_b,L)
                    else:
                        L.append(copy_b)
    return L

def generateHopping(bPosition):
    L=[]
    for a in range(len(bPosition)):
        if bPosition[a] == 'W':
            for b in range(len(bPosition)):
                if bPosition[b] == 'x':
                    copy_b = deepcopy(bPosition)
                    copy_b[a] = 'x'
                    copy_b[b] = 'W'
                    if checkMill(b, copy_b):
                        L = generateRemove(copy_b,L)
                    else:
                        L.append(copy_b)
    return L


def generateMovesMidgameEndgameBlack(bPosition):
    temp = reverse(bPosition)
    L = []
    moves = generateMovesMidgameEndgame(temp)
    for pos in range(len(moves)):
        b = moves[pos]
        L.insert(pos, reverse(b))
    return L

###########Improved Static Estimation###############

def countMills(b):
    possibleMills=0
    for pos in range(len(b)):
        if b[pos] == 'x':
            if improvedCount(pos,b,'W') == True :
                possibleMills+=1
    return possibleMills

def staticEstimateOpeningImproved(b):

    pieceDiff=staticEstimateOpening(b)
    possibleMills=countMills(b)


    return pieceDiff+possibleMills

def improvedCount(position,b,player):
    if (position == 0):
        if ((b[1] == player and b[2] == player) or (b[3] == player and b[6] == player) or (b[8] == player and b[20] == player)): return True
        return False
    elif (position == 1):
        if (b[0] == player and b[2] == player):return True
        return False
    elif (position == 2):
        if ((b[0] == player and b[1] == player) or (b[5] == player and b[7] == player) or (b[13] == player and b[22] == player)):return True
        return False
    elif (position == 3):
        if ((b[0] == player and b[6] == player) or (b[4] == player and b[5] == player) or (b[9] == player and b[17] == player)):return True
        return False
    elif (position == 4):
        if (b[3] == player and b[5] == player):return True
        return False
    elif (position == 5):
        if ((b[3] == player and b[4] == player) or (b[2] == player and b[7] == player) or (b[12] == player and b[19] == player)):return True
        return False
    elif (position == 6):
        if ((b[0] == player and b[3] == player) or (b[10] == player and b[14] == player)):return True
        return False
    elif (position == 7):
        if ((b[2] == player and b[5] == player) or (b[11] == player and b[16] == player)):return True
        return False
    elif (position == 8):
        if ((b[0] == player and b[20] == player) or (b[9] == player and b[10] == player)):return True
        return False
    elif (position == 9):
        if ((b[8] == player and b[10] == player) or (b[3] == player and b[17] == player)):return True
        return False
    elif (position == 10):
        if ((b[8] == player and b[9] == player) or (b[6] == player and b[14] == player)):return True
        return False
    elif (position == 11):
        if ((b[7] == player and b[16] == player) or (b[12] == player and b[13] == player)):return True
        return False
    elif (position == 12):
        if ((b[11] == player and b[13] == player) or (b[5] == player and b[19] == player)):return True
        return False
    elif (position == 13):
        if ((b[11] == player and b[12] == player) or (b[2] == player and b[22] == player)):return True
        return False
    elif (position == 14):
        if ((b[17] == player and b[20] == player) or (b[15] == player and b[16] == player) or (b[6] == player and b[10] == player)):return True
        return False
    elif (position == 15):
        if ((b[14] == player and b[16] == player) or (b[18] == player and b[21] == player)):return True
        return False
    elif (position == 16):
        if ((b[14] == player and b[15] == player) or (b[19] == player and b[22] == player) or (b[7] == player and b[11] == player)):return True
        return False
    elif (position == 17):
        if ((b[3] == player and b[9] == player) or (b[14] == player and b[20] == player) or (b[18] == player and b[19] == player)):return True
        return False
    elif (position == 18):
        if ((b[17] == player and b[19] == player) or (b[15] == player and b[21] == player)):return True
        return False
    elif (position == 19):
        if ((b[17] == player and b[18] == player) or (b[16] == player and b[22] == player) or (b[5] == player and b[12] == player)):return True
        return False
    elif (position == 20):
        if ((b[0] == player and b[8] == player) or (b[14] == player and b[17] == player) or (b[21] == player and b[22] == player)):return True
        return False
    elif (position == 21):
        if ((b[20] == player and b[22] == player) or (b[15] == player and b[18] == player)):return True
        return False
    elif (position == 22):
        if ((b[2] == player and b[13] == player) or (b[16] == player and b[19] == player) or (b[20] == player and b[21] == player)):return True
        return False
    else:
        return False

# Nine Men's Morris Game
**Technology: Python,Min-Max Algorithm, Alpha-Beta Pruning.**

The Morris Game, Variant , is a variant of Nine Men’s Morris game. It is a board game between two players: White and Black.The goal is to capture opponents pieces by getting three pieces on a single line (a mill). The winner is the first player to reduce the opponent to only 2 pieces, or block the opponent from any further moves. The game has three distinct phases: opening, midgame, and endgame.

Opening: Players take turns placing their 9 pieces - one at a time - on any vacant board intersection spot.

Midgame: Players take turns moving one piece along a board line to any adjacent vacant spot. Endgame: A player down to only three pieces may move a piece to any open spot, not just an adjacentone (hopping).

Mills: At any stage if a player gets three of their pieces on the same straight board line (a mill), then one of the opponent’s isolated pieces is removed from the board. An isolated piece is a piece that is not part of a mill.

The program consists of nine python files:

MiniMaxOpening: Implements the MiniMax algorithm to find the next move in the Opening Phase of game for white. 

MiniMaxGame: Implements the MiniMax algorithm to find the next move in the Mig/End Phase of game for white.

MiniMaxOpeningBlack:Implements the MiniMax algorithm to find the next move in the Opening Phase of game for black. 

MiniMaxGameBlack:Implements the MiniMax algorithm to find the next move in the Mig/End Phase of game for black.

MiniMaxOpeningImproved:Implements the MiniMax algorithm with Improvement to find the next move in the Opening Phase of game for white. 

MiniMaxGameImproved:Implements the MiniMax algorithm with Improvement to find the next move in the Mig/End Phase of game for white. 

ABOpening:Implements the AB algorithm to find the next move in the Opening Phase of game for white.

ABGame:Implements the AB algorithm to find the next move in the Mig/End Phase of game for white.

GameMove.py: Specifies Mills formation, difinition of neighbors and moves required in the board game

The program takes three agruments: board1.txt board2.txt 2

where board1.txt is the input board position, board2.txt is the output file location and 2 is the depth upto which the algorithm should run

Examples:

First program: MiniMaxOpening The first program plays a move in the opening phase of the game. For example, the input can be: (you type:) board1.txt board2.txt 2 (the program replies:) Board Position: xxxxxxxxxWxxWxxxBxxxxxx Positions evaluated by static estimation: 9. MINIMAX estimate: 9987. Here it is assumed that the file board1.txt content is: xxxxxxxxxWxxxxxxBxxxxxx The file board2.txt is created by the program, and its content is: xxxxxxxxxWxxWxxxBxxxxxx

Second program: MiniMaxGame The second program plays in the midgame/endgame phase. For example, the input can be: (you type:) board3.txt board4.txt 3 (the program replies:) Board Position: xxxxxxxxWWWxWWxBBBBxxxx. Positions evaluated by static estimation: 125. MINIMAX estimate: 9987. Here it is assumed that the file board3.txt exists and its content is: xxxxxxxxxxWWxWWxBBBxxxx The file board4.txt is created by the program, and its content is: xxxxxxxxWWWxWWxBBBBxxxx


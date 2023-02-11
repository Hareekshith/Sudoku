import sys
sys.path.append('D:/Programs/sudoku')

from module import startit, checkval
boardanswer = 0

def solution():
    global boardanswer
    boardanswer = startit.board.copy()
    found = [False]
    def solve(board, found):
        for i in range(9):
            for j in range(9):
                if board[i][j] == "-":
                    for num in range(1,10):
                        if checkval.possible(i, j, str(num)):
                            board[i][j] = str(num)
                            solve(board, found)
                            if found[0]:
                                return
                            board[i][j] = '-'
                    return
        startit.printboard(board)
        found[0] = True
        
    #solve(boardanswer, found)
    return boardanswer
from module import startit

def possible(x, y, num):
    global board
    for i in range(9):
        if startit.board[x][i] == num:
            return False
    for j in range(9):
        if startit.board[j][y] == num:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if startit.board[x0+i][y0+j] == num:
                return False
    return True

def validate(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != '-':
                if not possible(i, j, board[i][j]):
                    return False
    return True
from module import startit, checkval, answerfile

def placeit(x, y, num):
    if checkval.possible(x-1, y-1, num):
        startit.board[x-1][y-1] = num
        return True
    else:
        print("That's not possible!")
        return False


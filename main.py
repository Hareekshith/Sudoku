'''sudoku
table of 9 rows and columns
print some numbers in the table for the user to start with
then check if the user fills it correctly'''

import sys
sys.path.append('D:/Programs/sudoku')
from module import startit, answerfile, placevalues

print("""Welcome to Sudoku!
You will be given a partially filled table.
Fill in the rest of the table so that each row, column and 3x3 box contains the numbers 1 to 9.\n\n""")

print("""To put your values in the table, enter the row number and the column number with the number you desire. So table looks like this:
1,1|1,2|1,3|1,4|1,5|1,6|1,7|1,8|1,9
2,1|2,2|2,3|2,4|2,5|2,6|2,7|2,8|2,9
3,1|3,2|3,3|3,4|3,5|3,6|3,7|3,8|3,9
4,1|4,2|4,3|4,4|4,5|4,6|4,7|4,8|4,9
5,1|5,2|5,3|5,4|5,5|5,6|5,7|5,8|5,9
6,1|6,2|6,3|6,4|6,5|6,6|6,7|6,8|6,9
7,1|7,2|7,3|7,4|7,5|7,6|7,7|7,8|7,9
8,1|8,2|8,3|8,4|8,5|8,6|8,7|8,8|8,9
9,1|9,2|9,3|9,4|9,5|9,6|9,7|9,8|9,9 \n\n\n""")
answerfile.solution()
boardanswer = answerfile.boardanswer
vacant = 0
def checkvac():
    global vacant
    for rows in startit.board:
        for pl in rows:
            if pl == '-':
                vacant += 1
    return vacant

while True:
    startit.printboard(startit.board)
    checkvac()
    if vacant == 81:
        om = input("Do you want to start with a new board? (y/n): ")
        if om == 'y':
            quit()
        else:
            continue
    x = int(input("Enter the row number: "))
    y = int(input("Enter the column number: "))
    num = input("Enter the number: ")
    if boardanswer[x][y] == num:
        startit.board[x][y] = num
    else:
        print("Try another place!")
    checkvac()
    if vacant == 0:
        if startit.board == answerfile.boardanswer:
            print("You solved it!!!")
            break
    else:
        continue
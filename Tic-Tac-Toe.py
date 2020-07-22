global board
global FreeMoves
global moves_dict

def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ",board[i][0],"  |  ", board[i][1],"  |  ",board[i][2],"  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")
    


def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    found=True
    while (found == True and FreeMoves !=[]):
        user_move= int(input("Enter your next move please:"))
        index=moves_dict[user_move]
        if user_move > 0 and user_move < 10:
            if (board[index[0]][index[1]] == "X") or (board[index[0]][index[1]] == "O"):
                print("This move is chosen before, please choose another square")
                continue
            else:
                board[index[0]][index[1]]= "O"
                return "O"
                found=False
        else:
            found=True
            print("The entered number is not valid, choose a number between 1 and 9")
            continue


def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

    FreeFields=[]
    for i in range(3):
       for j in range(3):
          if (board[i][j]!="O") and (board[i][j] !="X"):
              FreeFields.append((i,j))
    FreeMoves=[]
    for i in range(len(FreeFields)):
        for key, value in moves_dict.items():
            if FreeFields[i] == value:
                FreeMoves.append(key)
    print("Free moves are:",FreeMoves)
    return FreeMoves
                



def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    from random import randrange

    FoundFree=False
    while (FoundFree==False and FreeMoves !=[]):
        Computer_Move=randrange(9)+1
        index=moves_dict[Computer_Move]
        for i in range(len(FreeMoves)):
            if Computer_Move  == FreeMoves[i]:
                board[index[0]][index[1]]= "X"
                FoundFree=True

        if (FoundFree==False):
            continue

    return "X"
                
    

   

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    victory=False
    for row in range(3):
        if (board[row][0] == sign) and (board[row][1] == sign) and (board[row][2] == sign):
           victory=True
    for column in range (3):
        if (board[0][column] == sign) and (board[1][column] == sign) and (board[2][column] == sign):
           victory=True
    if (board[0][0] == sign) and (board[1][1] == sign) and (board[2][2] == sign):
           victory=True
    if (board[0][2] == sign) and (board[1][1] == sign) and (board[2][0] == sign):
           victory=True

    if victory==True:
        if sign=="X":
            return "Computer"
        else:
            return "User"

    if (FreeMoves==[] and victory==False):
        return "There is no winner, the game ends with a tie."


#
# Main
#    
print("We are playing Tic-Tac-Toe. The Computer will make the first move. The board is")
board=[[1,2,3],[4,"X",6],[7,8,9]]
moves_dict={1:(0,0), 2:(0,1), 3:(0,2),4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
FreeMoves=[]

turn=True
while True:
    DisplayBoard(board)
    FreeMoves= MakeListOfFreeFields(board)
    if turn ==True:
        sign=EnterMove(board)
        turn=False
        winner=VictoryFor(board, sign)
        if winner==None:
            continue
        else:
            break
    
    if turn==False:
        sign=DrawMove(board)
        turn=True
        winner=VictoryFor(board, sign)
        if winner==None:
            continue
        else:
            break

DisplayBoard(board)
print("The winner is : The",winner)




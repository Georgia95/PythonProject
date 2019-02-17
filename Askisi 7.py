import random
valid=True
Choice = 'O'

board = [[' ', ' ', ' '],     # 00  01  02
         [' ', ' ', ' '],     # 10  11  12
         [' ', ' ', ' ']]     # 20  21  22
def winner(board):
    w=0
    for i in range(3):
        if(board[i-1][0]=='X' and board[i-1][1]=='X' and board[i-1][2]=='X'):
            w="COMPUTER"
        elif((board[i-1][0]=='O' and board[i-1][1]=='O' and board[i-1][2]=='O')):
            w =  "PLAYER 1"
    for i in range(3):
        if(board[0][i-1]=='X' and board[1][i-1]=='X' and board[2][i-1]=='X'):
            w = "COMPUTER"
        elif((board[0][i-1]=='O' and board[1][i-1]=='O' and board[2][i-1]=='O')):
            w =  "PLAYER 1"
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        w = "COMPUTER"
    elif ((board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O')):
        w =  "PLAYER 1"
    if (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        w = "PLAYER 1"
    elif ((board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O')):
        w = "COMPUTER"
    return  w
def checkvalid(thesi):
    if (thesi=="00" or thesi=="01" or thesi=="02" or thesi=="10" or thesi=="11" or thesi=="12" or thesi=="20" or thesi=="21" or thesi=="22"):
        return True
    else:
        return False
def StartGame(board):

    round = 0
    Player = "human"
    while round!=9:
        if(Player == "human"):
            thesi = input("Give position  ")
            valid= checkvalid(thesi)
            while(valid==False):
                    print ("not valid input, plese insert position  ")
                    thesi = input("Give position  ")
                    valid = checkvalid(thesi)
            x = int(thesi[0])
            y = int(thesi[1])
            if (board[x][y] == ' '):
                    board[x][y] = 'O'
                    print (board[0])
                    print (board[1])
                    print (board[2])
                    round+=1
                    win= winner(board)
                    if(win=="PLAYER 1"):
                        print ("Winner", win)
                        break
                    else:
                        Player = "Computer"

        elif (Player=="Computer"):
            x = random.randint(0,2)
            y = random.randint(0,2)
            print ("computer turn! position", x, y)
            if (board[x][y] == ' '):
                board[x][y] = 'X'
                print (board[0])
                print (board[1])
                print (board[2])
                round += 1
                if (win == "COMPUTER"):
                    print ("Winner", win)
                    break
                else:
                    Player = "human"

StartGame(board)
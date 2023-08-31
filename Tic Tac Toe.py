#Mehki Agudo
from random import *

board = [["","",""],["","",""],["","",""]]
for row in board:
        print(row)
def playermove():
        while True:
                row = int(input("pick row 1, 2, or 3: "))-1
                column = int(input("pick column 1, 2, or 3: "))-1

                if board[row][column] == "x" or board[row][column] == "o":
                        print("pick a spot that isn't taken")
                        continue
                else:
                        break
        board[row].pop(column)
        board[row].insert(column,"x")
def compmove():
        while True:
                compRow = (randint(0,2))
                compColumn = (randint(0,2))
                if board[compRow][compColumn] == "x" or board[compRow][compColumn] == "o":
                        continue
                else:
                        break
        board[compRow].pop(compColumn)
        board[compRow].insert(compColumn,"o")
        #win fuction
def winnerWinner():
        while True:
                if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x" or board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x" or board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x" or board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x" or board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x" or board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x" or board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x" or board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
                        print("x wins")
                        break
                elif board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o" or board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o" or board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o" or board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o" or board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "o" or board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o" or board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o" or board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o":
                        print("o wins")
                        break
                else: 
                        print("looks like a tie")
                        break
while True:
        playermove()
        compmove()
        print(" ")
        winnerWinner()
        for row in board:
                print(row)
                

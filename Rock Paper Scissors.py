from random import *


x=1
def game(x):
    print("the game goes first to 2 ws and the first game is practice")
    list=["rock","paper","scissor"]
    cpu=choice(list)
    user=input("choose rock, paper, or scissors: ")
    print("the cpu chose",cpu)
    w=0
    l=0
    while w+l<3:
        user=input("choose rock, paper, or scissors: ")
        cpu=choice(list)
        print(cpu)
        if user=='rock' and cpu=='scissor' :
            print("you w")
            w=w+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        elif user=="paper" and cpu=="rock":
            print("you w")
            w=w+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        elif user=="scissor" and cpu=="paper":
            print("you w")
            w=w+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        elif user=="paper" and cpu=="scissor":
            print("you l")
            l=l+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        elif user=="scissor" and cpu=="rock":
            print("you l")
            l=l+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        elif user=="rock" and cpu=="paper":
            print("you l")
            l=l+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        elif user==cpu:
            print("tied")
            l=l+1
            print("you have ", w, " ws and the cpu has ", l, " ws")
        if w==2:
            print("congrats you w!!!")
        elif l==2:
            print("dang you lost")
game(x)

       


    






#use a while loop to keep asking you to play if you lost

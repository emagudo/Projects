#Mehki Agudo 3/8/2023


#Sets x to a random number between 0 and 100 and ask the user to guess the number until the number is found
from random import *

x=randrange(0,100)
y=int(input("Guess the random number from 0-100: "))
z=1
if x==y:
    print("correct, the number was ",x)
while y!=x:
    if y>x:
        print("that answer was too big guess again")
        y=int(input("Guess the random number from 0-100: "))
        z=z+1
    elif y<x:
        print("that answer was too small guess again")
        y=int(input("Guess the random number from 0-100: "))
        z=z+1

if x==y:
    print("correct, the number was ",x, "you guessed it in ",z, " tries")
    
    

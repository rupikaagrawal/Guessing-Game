import random

chances=0

cguess=random.randint(0,9)

while chances < 5:
    guess=int(input("between 0 to 9 guess a number: "))
    if guess==cguess:
       print("Congratulations you win")
       break
    elif guess<cguess:
         print("The number you guessed is smaller \n")
    else:
         print("The number you guessed is higher \n")
    chances=chances+1
if not chances < 5:
    print("You loss, the number is ",cguess)
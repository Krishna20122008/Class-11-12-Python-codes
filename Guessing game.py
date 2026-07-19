import random

print("Welcome to the guessing game!!")
number=random.randrange(0,100)

while True:
    userinput=int(input(("Enter a number to guess: ")))
    if userinput<number:
        print("Sorry, you guessed it wrong.... Go a little higher.")
    elif userinput>number:
        print("Sorry, you guessed it wrong.... Go a little lower.")
    else:
        print("Yay!! You guessed it right.. CONGRATS !!")
    
def stonepaperscissor():
    print("Welcome to the Rock Paper Scissor Game!!!")

    import random

    while True:
        a= random.choice(['Stone', 'Paper', 'Scissor'])

        userinput=input("Stone / Paper / Scissor : ").capitalize()
        
        if userinput=='Stone' and a=='Stone': 
            print(f"You: {userinput} and computer: {a} , so try again") 
            continue

        if userinput=='Paper' and a=='Paper': 
            print(f"You: {userinput} and computer: {a} , so try again")
            continue

        if userinput=='Scissor' and a=='Scissor': 
            print(f"You: {userinput} and computer: {a} , so try again") 
            continue

        if userinput=='Stone' and a=='Paper': 
            print(f"You: {userinput} and computer: {a} , Computer Won!!")
            break

        if userinput=='Scissor' and a=='Stone': 
            print(f"You: {userinput} and computer: {a} , Computer Won!!")
            break

        if userinput=='Paper' and a=='Scissor': 
            print(f"You: {userinput} and computer: {a} , Computer Won!!")
            break

        elif userinput not in ("Stone", "Paper", "Scissor"): 
            print(f"You: {userinput} and computer: {a} , Write appropriate answer !!")
            continue

        else: 
            print(f"You: {userinput} and computer: {a} , User Won!!")
            break
            

    print("Thanks for playing stone paper scissor game!!")

while True:
    b=input("Do you want to play the game ? (y/n): ")
    if b=="y":
        stonepaperscissor()
    if b=="n":
        print("Thankyou!")
        break

input("Press any key to exit the game: ")
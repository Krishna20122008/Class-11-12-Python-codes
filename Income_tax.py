#This is a python code to find the income tax of a person..
a=(input("Are you a politician? y/n:"))

if a=="y":
    print("You don't have to pay any tax.")

elif a=="n":
    print("Then you are a salary receiver.")

    i=int(input("Enter your Income:"))

    if i<=50000:
        print("The tax you have to pay is:₹",  (i*0.005))

    elif i>50000 and i<=100000:
        print("The tax you have to pay is:₹",(i*0.2))

    elif i>=120000:
        print("The tax you have to pay is:₹",(i*0.5))

input()





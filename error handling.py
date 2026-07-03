print("Trying try and except block..")
while True:
    try:
        a=int(input("Enter the number you want to divide with:"))
        numerator=50
        quotient=numerator/a
        print(f"The answer on dividing {a} by 50 is {quotient}")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except TypeError:
        print("Enter the number in integer.")
    except:
        print("Any other error..")
    finally:
        print("Thanks for using try and except block..")

    b=input("Do you want to continue? (y/n)")
    if b=="y":
        continue
    elif b=="n":
        break
    else:
        print("Answer in y/n")

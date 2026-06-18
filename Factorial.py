#This is a python code to find the factorial of a number entered by the user..

n=int(input("Enter your number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("The value of factorial of",n,"is: ",fact)

#This is a code to get the multiplication table of a number entered by user

num= int(input("Enter the number whose table you want to know: "))

for x in range(1,99):
    y=x*num
    print(f"{num} X {x} = {y}")
   
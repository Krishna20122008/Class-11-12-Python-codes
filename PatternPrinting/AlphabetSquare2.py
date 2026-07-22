a = int(input("Enter no. of rows: "))
b = int(input("Enter no. of columns: "))
ascii = 97 + a

for i in range(97,ascii+1):
    for j in range(1,b+1):
        print(chr(i), end = " ")
    print()
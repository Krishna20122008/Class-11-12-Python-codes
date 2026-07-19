a = int(input ("Enter the number of sides: "))
ascii = 65+a

for i in range(1,a+1):
    for j in range(65,ascii+1):
        print(chr(j), end = "  ")
    print()
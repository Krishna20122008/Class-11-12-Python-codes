def linearsearch(list,key):
    for i in range(0,len(list)):
        if list[i]==key:
            return i+1
        else:return None

list=[]
max=int(input("How many elements are there in your list?"))
print("Enter each element and press enter:")
for i in range(0,max):
    n=int(input())
    list.append(n)
print("The list is: ", list)
key=int(input("Enter the number to be searched: "))
position=linearsearch(list,key)
if position is None:
    print("No key present")
else:
    print("Key is at position: ", position)
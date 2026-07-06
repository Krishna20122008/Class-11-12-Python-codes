def binarysearch(list,key):
    first=0
    last=len(list)-1
    while(first<=last):
        mid=(first+last)//2
        if list[mid]==key:
            return mid
        elif key>list[mid]:
            first=mid+1
        elif key<list[mid]:
            last=mid-1
        
    return -1

list=[]
print("Create a list by entering elements in ascending order: ")
print("press enter after each element, press -999 to stop entering")
num=int(input())
while num!=-999:
    list.append(num)
    num=int(input())
n=int(input("Enter the key to be searched: "))
pos=binarysearch(list,n)
if (pos!=-1):
    print("The entered key is at position",pos+1)
else:
    print("The key is not found in the list")
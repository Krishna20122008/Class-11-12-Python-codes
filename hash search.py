def hashfind(key,hashtable):
    if (hashtable[key%10]==key):
        return((key%10)+1)
    else:
        return None
    
hashtable=[None,None,None,None,None,None,None,None,None,None]
print("We have created a hashtable of 10 positions: ")
print(hashtable)
L=[34,16,2,93,80,77,51]
print("the given list is", L)

for i in range(0,len(L)):
    hashtable[L[i] % 10] = L[i]

print("The hashtable contents are: ")
for i in range(0,len(hashtable)):
    print("hashindex=", i,", value =", hashtable[i])

key=int(input("Enter the number to be searched:"))
position=hashfind(key,hashtable)
if position is None:
    print("key not found")
else:
    print("position=", position)
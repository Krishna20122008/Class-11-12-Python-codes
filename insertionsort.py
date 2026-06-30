def insertionsort(list):
    n=len(list)
    for i in range(1,n):
        key=list[i]
        j=i-1
        while j>=0 and list[j]>key:
            list[j+1]=list[j]
            j=j-1

        list[j+1]=key
    print(list)

list=[5,6,3,6,2]
insertionsort(list)

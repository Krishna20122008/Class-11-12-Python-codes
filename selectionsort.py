def selectionsort(list):
    n=len(list)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if list[j]<list[minindex]:
                minindex=j
        list[i],list[minindex]=list[minindex], list[i]

    print("The sorted list is", list)

list=[4,6,-2,-5,5,4]
print("The given list is: ", list)
selectionsort(list)
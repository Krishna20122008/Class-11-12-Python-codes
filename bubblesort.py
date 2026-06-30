def bubblesort(list):
    n=len(list)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)

list=[4,2,5,-2,748]
bubblesort(list)

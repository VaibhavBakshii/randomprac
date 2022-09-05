l1=[1,2,3,4,5,6,54,454,5,345,4,54,54,5,34,3,432,4]
n=len(l1)
for i in range(0,n):
    for j in range(0,n-1-i):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
        print(l1)

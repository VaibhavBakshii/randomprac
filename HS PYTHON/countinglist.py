l1=[1,2,3,4,1,2,3,4,5,6]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
for eachunique in l2:
    c=1
for value i in l1:
        if eachunique==value:
            c+=1
            print(eachunique,'occur',count,'times')
            


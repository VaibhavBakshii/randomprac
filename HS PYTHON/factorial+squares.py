x=int(input('enter the number'))
n=int(input('enter the number'))
p=1
f=1
c=int(input('enter the value'))
for i in range(1,n+1,1):
    p*=x
    break
for i in range(1,c+1,1):
    f*=i
    print(p//f,end=',')




    

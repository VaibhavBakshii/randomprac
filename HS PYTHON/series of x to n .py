x=int(input('enter the value'))
n=int(input('enter the number'))
p=1
for i in range(1,n+1,1):
    p*=x
    print(p,end=',')

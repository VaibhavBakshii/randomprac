l1=[]
n=int(input('enter the score'))
if n%10==0:
    score=(n+10)
    l1.append(score)
    print(l1)
elif n%5==0:
        score=(n+5)
        l1.append(score)
        print(l1)
else:
    score=n+2
    l1.append(score)
    print(l1)

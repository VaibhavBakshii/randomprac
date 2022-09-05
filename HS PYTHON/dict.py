d={}
l1=[1,2,3,4]
l2=['roshan','rohan','ritesh','rajnish']
print(sorted(l2))
for i in range (len(l1)):
    d[l1[i]]=l2[i]
print(d)
d[0]='rakesh'
print(d)
d.pop(2)
print(d)

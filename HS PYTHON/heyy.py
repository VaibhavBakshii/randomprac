str=input('enter the string')
ca=0
cdi=0
for i in range(0,len(str)):
    if(str[i]>='A' or str[i]=='Z'):
        ca=ca+1
else:
    if(str[i]>='0' or str[i]=='9'):
        cdi=cdi+1
print('no.of words are',ca)
print('no.of uppercase are',cdi)

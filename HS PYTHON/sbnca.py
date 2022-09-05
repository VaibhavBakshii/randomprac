ans='y'
items={}
vals=[]
final={}
while ans=='y':
    key=input('enter the item')
    value=int(input('enter the price'))
    items[key]=value
    vals.append(value)
    ans=input('press y to continue')
    vals.sort(reverse=True)
    found=[]
    for x in vals:
        for i in items:
            if x==items[i]:
              final[i]=x
        print(final)
    
    
    
    
    

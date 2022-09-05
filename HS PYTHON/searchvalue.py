l1=[10,35,16,25,35,12,19]
search=int(input('enter the value to be searched'))
found=1
i=0
while i<len(l1) and not found:
    if search==l1[i]:
        found=0
    l+=1
    if found:
        print(search,'found at',i)
    else:
        print('sorry not found')

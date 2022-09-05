a=int(input('enter number of students who wear size 7'))
b=int(input('enter number of students who wear size 6'))
c=int(input('enter number of students who wear size 5'))
if a>b and a>c:
    print('Manafacture size 7 shoes')
elif b>a and b>c:
    print('manafacture size 6 shoes')
elif c>a and c>b:
    print('Manafacture size 5 shoes')
elif a==c and b==c:
    print('manafacure all')
else:
    print('order cancelled')



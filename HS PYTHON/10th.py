a=input('enter your name')
b=int(input('enter the marks in science'))
c=int(input('enter the marks in math'))
d=int(input('enter the marks in english'))
e=int(input('enter the marks in social science'))
f=int(input('enter the marks in hindi/French'))
g=((b+c+d+e+f)/5)
print('average is',g)
h=((c+b+d+e+f)/500)*100
print('your percetage is',h)
if h>=90:
    print('Excellent',a)
elif h<90 and h>=80:
    print('good',a)
elif h<80 and h>=70:
    print('average',a)
else:
    print(a,'could have done much better')

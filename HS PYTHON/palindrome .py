num=int(input('enter the number'))
temp=num
s=0
while temp!=0:
    s=(s*10)+(temp%10)
    temp=temp//10
if num==s:
    print(s,'is a palindrome')
else:
    print(s,'is not a palidrome')

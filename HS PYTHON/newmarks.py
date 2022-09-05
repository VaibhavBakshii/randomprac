a=int(input('enter the marks'))
if a>90:
    newmarks=(a+(a*0.02))
elif a>=71 and a<=90:
    newmarks=(a+(a*0.04))
elif a>=51 and a<=90:
    newmarks=(a+(a*0.06))
elif a<=50:
    newmarks=(a)
else:
    newmarks=marks
    print('no extra marks are given')
print('new marks are',newmarks)

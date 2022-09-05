x="water"
a=len(x)-1
for i in range(a):
    print(''*i+x[i]+''*((2-a)-1-(2*i))+x[i])
print(''*(i+1)+x[i+1])

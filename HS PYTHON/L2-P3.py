# List-Program No : L2-P3
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

L =[1,2,3,4,5,6,7,8]

#AddingValuesToList

def AddValues(L):
    while True:
        value = int(input('Enter The Value to be added in the list L'))
        L.append(value)
        cont = input('Add More(Y/N)')
        if cont in ['N','n']:
            break
    print('List is:', L)
    
#DisplayingTheValues
    
def DispValues(L):
    print('Values of List L:', L)
    
#DisplayReversedValues
    
def RevContent(L):
    print('Values Reversed in the list L:', (L[::-1]))

#AddAllEvenValues

def AddEven(L):
    T = 0
    for S in L:
        if S % 2 == 0:
            T += S
    print('Sum of even elements of List L:', T)

def AddOdd(L):
    T = 0
    for S in L:
        if S % 2 != 0:
            T += S
    print('Sum of odd elements of list L:', T)

def AddZeroEnd(L):
    T = 0
    for S in L:
        if str(S)[-1] == '0':
            T += S
    print('Sum of zero elements of list L:', T)

def Show7Ten(L):
    T = []
    for S in L:
        if S // 10 == 7:
            T.append(S)
    print('Values in List L having 7 at Tens Place', T)

def Show20_50(L):
    T = []
    for S in L:
        if 20 <= S <= 50:
            T.append(S)
    print('Values in List between 20 and 50 are:', T)
    
AddValues(L)
DispValues(L)
RevContent(L)
AddEven(L)
AddOdd(L)
AddZeroEnd(L)
Show7Ten(L)
Show20_50(L)

"""Enter The Value to be added in the list L5
Add More(Y/N)N
List is: [1, 2, 3, 4, 5, 6, 7, 8, 5]
Values of List L: [1, 2, 3, 4, 5, 6, 7, 8, 5]
Values Reversed in the list L: [5, 8, 7, 6, 5, 4, 3, 2, 1]
Sum of even elements of List L: 20
Sum of odd elements of list L: 21
Sum of zero elements of list L: 0
Values in List L having 7 at Tens Place []
Values in List between 20 and 50 are: []"""



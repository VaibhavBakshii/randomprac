# List-Program No : L2-P1
# Developed By : Vaibhav Bakshi
# Date : 12/01/21

E = []
M = []
T = []

for i in range (1,6):
    e = int(input('Enter English Marks of Student (i)'))
    m = int(input('Enter Mathematics Marks of Student (i)'))
    E.append(e)
    M.append(m)
    T.append(e+m)

#Content
    
print("Content of E:", E)
print("Content of M:", M)
print("Content of T:", T)

#Maximum

print("Maximum Marks of E:", max(E))
print("Maximum Marks of M:", max(M))
print("Maximum Marks of T:", max(T))

#Minimum

print("Minimum Marks of E:", min(E))
print("Minimum Marks of M:", min(M))
print("Minimum Marks of T:", min(T))

#Average

print("Average Marks of E:", sum(E)/len(E))
print("Average Marks of M:", sum(M)/len(M))
print("Average Marks of T:", sum(T)/len(T))



"""
Output

Enter English Marks of Student (i)5
Enter Mathematics Marks of Student (i)10
Enter English Marks of Student (i)15
Enter Mathematics Marks of Student (i)20
Enter English Marks of Student (i)25
Enter Mathematics Marks of Student (i)30
Enter English Marks of Student (i)25
Enter Mathematics Marks of Student (i)25
Enter English Marks of Student (i)30
Enter Mathematics Marks of Student (i)30
Content of E: [5, 15, 25, 25, 30]
Content of M: [10, 20, 30, 25, 30]
Content of T: [15, 35, 55, 50, 60]
Maximum Marks of E: 30
Maximum Marks of M: 30
Maximum Marks of T: 60
Minimum Marks of E: 5
Minimum Marks of M: 10
Minimum Marks of T: 15
Average Marks of E: 20.0
Average Marks of M: 23.0
Average Marks of T: 43.0
"""






#finding eucledian distance between two points
import math as  mt

list1=[]
for i in range(2):
    j=int(input("enter coordinate "))
    list1.append(j)
print(list1)   

list2=[]
for i in range(2):
    j=int(input("enter coordinate "))
    list2.append(j)
print(list2)   

# for i in range(2):
x=list2[0]-list1[0]
y=list2[1]-list1[1]
distance = mt.sqrt((x**2)+(y**2))
    
print(distance, "is the distance between points ", list1, " and ", list2)
num=int(input("Hello! input number of ages you want to check for "))
list1=[]
for i in range(num):
    j=int(input("enter number "))
    list1.append(j)
    #extend works to add 2 list together and not add element to list
k=-1 
for i in range(num):
    if(list1[i]>k):
        k=list1[i]
print(k, "is the largest age")

#~~~~~~~~~~~~~~~~~~ another method ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# num1=int(input("Enter 1st age   "))
# num2=int(input("Enter 2nd age   "))

# if num1>num2:
#     temp=num1
# else:
#     temp=num2

# num3=int(input("Enter 3rd age   "))
# if num3>temp:
#     print(num3,"    is the largest")
# else:
#     print(temp,"    is the largest")


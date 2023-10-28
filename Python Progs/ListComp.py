'''
list comprehension formulae
mylist = [1, 2, 3, 4, 5, 6]
newlist = [i*10 for i in mylist]

instead of using for loop we use list comprehension which is faster

'''
# ----------------------------------------------------------------------- #
'''
Given dictionary is consisted of vehicles their weights in kilograms. 
Contruct a list of the names of vehicles with weight below 5000 kilograms. 
In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# explains a lot about list comprehension!

lst=[i.upper() for i in dict if dict[i]<5000]

print(lst)

'''
# ----------------------------------------------------------------------- #
'''
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k 
is not equal to n. Here, i,j,k belongs in [0,x/y/z] range

x = int(input())
y = int(input())
z = int(input())
n = int(input())


lst1 = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]

print(lst1)

'''
# ----------------------------------------------------------------------- #
'''
n = int(input())
arr = map(int, input().split())

# set1 = set(arr)
# lst1=[]
# for i in set1:
#     lst1.append(i)
# lst2=sorted(lst1)
# print(lst2[len(lst2)-2]) 

print (sorted(set(arr))[-2])            # MIND BLOWING SOLUTION!!!!! ALL ABOVE # STEPS IN 1 STEP!!!!!!

'''
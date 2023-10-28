# print if 2 given rectangle (coordinates of diagonal corners given) are overlapping
# condition: rectangle sides are parallel to coordinate axes

print("Enter the x,y coordinates of first rectangle ")
Rect1=[]
Rect2=[]

c1=input("L1 coordinates  ") #coordinates of left point of Rect1
c2=input("R1 coordinates  ") #coordinates of right point of Rect1

Rect1.append(c1.split(","))
Rect1.append(c2.split(","))

c3=input("L2 coordinates  ")
c4=input("R2 coordinates  ")

Rect2.append(c3.split(","))
Rect2.append(c4.split(","))

print(Rect1, " are coordinates of rectangle 1 ")
print(Rect2, " are coordinates of rectangle 2 ")

if int(Rect2[0][0]) in range(int(Rect1[0][0]), int(Rect1[1][0])):
    print("overlapping")
elif int(Rect2[0][1]) in range(int(Rect1[0][1]), int(Rect1[1][1])): 
    print("overlapping")
else:
    print("bruh")    
    
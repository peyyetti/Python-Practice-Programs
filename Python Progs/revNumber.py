#reversing a number and checking for pallindrome

num=input("Hello! enter the number you want to reverse ")
copy1=int(num)
copy2=copy1
# list1=[]
sum=0
for i in range(len(num)):
    k=int(copy1%10)
    copy1=copy1/10
    sum=sum*10+k
if sum==copy2:
    print("number", sum, "is pallindrome for", copy2)
else:
    print("reverse of ", copy2, "is ", sum)    
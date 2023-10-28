#Check if given 4-digit number is narcissist number or not
# basically the number should be equal to sum of all digits raised to power of number of digits\
    
# 1634 ---> 1^4 + 6^4 + 3^4 + 4^4 = 1634  => narcissist number

num=int(input(("Enter a number ")))
holder=num
sum = 0

for i in range(4):
    temp=int(num%10)
    sum=sum+pow(temp,4)
    num=(num/10)

if(sum==holder):
    print(sum, " is a narcissist number ")    
else:
    print(sum, " is not a narcissist number ")    
    
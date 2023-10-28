# extract username from gmail like: pavankartik10@gmail.com ----> pavankartik10 is username

# method 1
def method1():
    email=input("Enter email id ")
    store=email.split("@")

    print(store[0])

# method 2
def method2():
    email=input("Enter email id ")
    index=email.find("@")
    
    for i in range(index):
        print(email[i], end="")
        

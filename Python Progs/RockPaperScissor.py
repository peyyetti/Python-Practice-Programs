# Rock, paper, scissor game

# consider rock = 0, paper = 1, scissor = 2

import random as rd

def random():
    mylist = [0,1,2]
    rd.shuffle(mylist)
    
    return mylist[0]

compIP = random()

userIP = int(input("Enter 0 for rock, 1 for paper, 2 for scissor "))

print("User input is ", userIP, " and computer input is ", compIP)

output = userIP - compIP

print(output)

if(output==0):
    print("Draw! ")
elif(output == 1) or (output == -2):
    print("User Wins! ")
else:
    print("User Loses! ")
# converting string to title case

def usingTitle():
    string=input("Enter a string ")
    print(string.title())

def noTitle():
    string=input("Enter a string ")
    words=string.split()
    templist=[]
    
    for i in range(len(words)):
        element=words[i]
        templist.append(list(element))
        
        temp=templist[i][0].upper()
        templist[i][0]=temp
    for j in range(len(templist)):
        for k in range(len(templist)):
            print(templist[j][k], end="")
    
    # for word in words:
    #     for letter in word:
    #         letter=letter.upper()    
    #         break                   # so that only 1st letter becomes upper case
        
    # print(words)
noTitle()
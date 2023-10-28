# program to remove a particular character from a string
def removeChar():
    str1 = input("Enter a string ")
    ch = input("Enter a character you want to remove from string ")

    new_str1 = str1.replace(ch,"")

    print(new_str1)


# program to remove duplicates from a list
def removeDuplicate():
    lst1 = [1, 4 , 1 , 6, 7, 223, 189, 92, 1, 4, 6, 223]

    new_set = set(lst1)

    lst2 = []

    for element in new_set:
        lst2.append(element)    

    print(lst2)


# program to check if a string is a pallindrome 
def strPallindrome():
    sen = input("Enter the string to check for palindrome ")

    lst1 = []
    for word in sen:            # creating list of letters in the string
        lst1.append(word)

    lst2 = lst1.copy()          # copying the old list to create a new reversed list
    lst2.reverse()

    tenz = ""   
    for element in lst2:        # creating a reversed string by joining elements in reversed list 
        tenz = tenz + element

    if (sen == tenz):
        print("pallindrome!!")
    else:
        print("Not pallidrome ")


# program that can find the most used word in a bollywood song
def most_used_lyric():
    song = input("Enter the lyrics of the song ")
    lst1 = song.split(" ")              # splitting the words into individual elements

    s1 = set(lst1)                      # converting list to set to get all unique elements

    libr = {}
    for element in s1:                  # set traversal and addition of key(element) to its value(count of element)
        libr[element] = lst1.count(element)

    num = max(libr.values())            # finding maximum value in dictionary

    for key, val in libr.items():       # splitting key-value pair into indiv components using items() method
        if val==num:
            print(f"{key} is the most used word. No of instances = {num} \n")

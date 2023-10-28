#angle between hour and minute hand

H=int(input("Hello! input hour hand position "))
M=int(input("Hello! input minute hand position "))

m=M*6       # in 1 minute, minute hand move 6degree, then in M min it moves---
h=H*30 + M*0.5      #in 1 hour, hour hand moves 30degree, and also in 1 min it moves 0.5 degree(***)

# (***) here we have taken that in 1 hour, min value range from 0-59, this angle also need to be counted

angle=abs(h-m)
if angle<180:
    print(f"angle between hour and minute hand is {angle} degrees")
else:    
    print(f"angle between hour and minute hand is {360-angle} degrees")
    
#another approach
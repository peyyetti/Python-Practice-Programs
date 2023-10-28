# given numerator and denominator, we have to give simple fraction

numr=int(input("Enter Nr "))
denm=int(input("Enter Dr "))

# we try to find the HCF of numr and denm
hcf=1
smaller=0
# trying to find numr is greater or denm, to determine if proper fraction or not
if(numr>denm):
    smaller=denm
else:
    smaller=numr

for i in range(1, smaller+1):
    if(numr%i==0) and (denm%i==0):
        hcf=i

print(f"HCF of {numr} and {denm} is {hcf}")

# now we divide numr and denm with HCF to get smaller possible fractions

numr=int(numr/hcf)
denm=int(denm/hcf)

print(f"Fraction value is {numr}/{denm}")
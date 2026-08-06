import math
n=int(input("Enter no."))
a=int(math.sqrt(n))
c=0

for i in range(2,a+1):
    if n%i==0:
        
        c+=1
    
if c>1:
    print("prime")

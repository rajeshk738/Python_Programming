"""
Input : 6

output
*
**
***
****
*****
******
*****
****
***
**
*


"""

""" First solution
no  = int(input())

z = no

for i in range(0,no):
    for j in range(0,no):
        print("*",end='')
        if(i==j):
            break
    print()    

for i in range(0,no-1):
    z = z-1
    for j in range(0,z):
        print("*",end='')   # by default p
    print()
"""

n = int(input("Please enter an integer: "))
for x in range(1, n+1):
    print("*" * x)
for y in range(n-1, 0, -1):
    print("*" * y)
        
        
        

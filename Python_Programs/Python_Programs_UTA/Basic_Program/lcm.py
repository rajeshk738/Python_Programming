import math

x=int(input("enter 1st number: "))
y=int(input("enter 2nd number: "))
gcd=math.gcd(x,y)
lcm=str((x*y)/gcd)
print("Lcm result: "+lcm)


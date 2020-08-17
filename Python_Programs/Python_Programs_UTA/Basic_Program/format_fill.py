# different format filling


my_str = "x = {} and y = {}".format(5,10)
print(my_str)

print("--------------------------------------------------")
my_str = "x = {0} and y = {0} and z = {1}".format(5,10)
print(my_str)

print("--------------------------------------------------")
my_str = "x = {0:3d} and y = {1:6.3f} ".format(5,10.5)
print(my_str)

print("--------------------------------------------------")
my_str = "x={0:x<6d} and y={1:z>7d}".format(72,38)
print(my_str)
print("--------------------------------------------------")
my_str = "x = {0:*<6s} and y = {1:#^7s}".format("Dog","cat")
print(my_str)

print("--------------------------------------------------")

s = 123456789
p = 23.98876543
my_str = "x={0:*<6d} and y={1:#^10.5f}".format(s,p)
print(my_str)

print("--------------------------------------------------")

# sign parameter

my_str = "x = {0:5.3f} and y = {0:+5.3f}".format(9.67)
print(my_str)

print("--------------------------------------------------")

# space before number
my_str = "x = {0:3d} and y = {0: 3d}".format(9)
print(my_str)


print("--------------------------------------------------")

my_str = "x = {1:A^+11.3f}".format(43,12.345678)
print(my_str)

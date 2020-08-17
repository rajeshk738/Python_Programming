# to check the given is list or not
from builtins import list

names = ["rajesh","lokesh",[10,20,30],[2.5,'ra',5],'ramesh']

print(isinstance(names, list))

print(isinstance(names[0], list))

print(isinstance(names[2], list))

print("\n\nprinting the nested elements")

for i in names:
    if isinstance(i, list):
        for j in i:
            print(j)
    else:
        print(i)        
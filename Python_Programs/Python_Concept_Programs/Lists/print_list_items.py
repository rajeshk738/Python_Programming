
names = ["rajesh","lokesh",[10,20,30],[2.5,'ra',5],'ramesh']

print(names)

print(names[2][2])

print(" ")
# printing all list items

for i in names:
    print(i)

print(" ")
    
# printing items in the same line we should use end=''
print("List items: ")
for i in names:
    print(i,end='')
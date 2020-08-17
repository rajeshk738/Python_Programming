# program to demonstrate displaying a class roll.

my_course = [["Buny",100,87,95],["Duck",78,9,89],["Rubb",83,85,92]]


for student in my_course:
    for item in student:
        if(type(item) == str):
            print("{0:10s} | ".format(item),end='')
        else:
            print("{0:3d} | ".format(item),end='')
    print("")        

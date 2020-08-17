# this function prints boundary traingle of height h

def boundary_traingle(h):
    i = 1
    j = 3
    str = "*"
    str1 = " "
    print(str*h)

    while(i<h):
        if(i == h-1):
           print(str)
           break
        print(str,end='')
        if(h != j):
            print(str1*(h-j),end='')
        j = j + 1
        print(str)
        i = i + 1


print(boundary_traingle(1))


"""

# This is another solution

n = int(input("Please enter a positive integer: "))
if n > 1:
    print (n*"*") # Print the top line
    for x in range(n-1, 1, -1):
        print("*"+ (x-2)*" "+"*") # Print the middle lines
    print("*") #print the bottom line
elif n == 1:
    print("*")


"""    
    

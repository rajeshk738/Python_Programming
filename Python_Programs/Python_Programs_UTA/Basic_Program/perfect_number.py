# perfect number program

def perfect_number(a):
    sum = 0
    i = 1
    while(i<a):
        if(a%i == 0):
            sum = sum + i
        i = i + 1        
    if(sum == a):
        print("Perfect number")
    else:
        print("Not a perfect number")

perfect_number(6)
perfect_number(8)
perfect_number(24)

    
    

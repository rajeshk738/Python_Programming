def calculate_gcd(a,b):
    if b == 0:
        return a;
    
    else:
        return calculate_gcd(b, a%b)
    
    
print(calculate_gcd(8, 20))    
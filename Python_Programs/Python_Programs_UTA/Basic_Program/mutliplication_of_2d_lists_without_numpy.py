def product(a,b):
    c = [[],[]]
    k = 0
    sum = 0
    l = -1
    
    if len(a[0])==len(b):
        for a_rows in a:
            for i in range(0,len(b[0])):
                sum = 0
                for j in range(0,len(b)):
                    sum = sum + a_rows[j] * b[j][i]  
                c[k].append(sum)
            k = k + 1   
            
    else:
        print("not possible")
    return c        
        
                           
                               
            
    


a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print(product(a,b))
		
		
    

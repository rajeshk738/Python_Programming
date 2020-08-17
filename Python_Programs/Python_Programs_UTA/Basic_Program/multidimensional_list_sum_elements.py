
def sum_multidimensional_list(m):
    sum = 0
    
    for i in range(0,len(m)):
        
        for j in range(0,len(m[0])):
            sum = sum + m[i][j]

    return sum



m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[15,14,15]]

print("sum = ",sum_multidimensional_list(m))

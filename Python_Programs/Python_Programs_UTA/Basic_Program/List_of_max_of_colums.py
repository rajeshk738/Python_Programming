
def count_column_max(m):
    max_count = 0
    count = 0
    new_list = []
    
    for i in range(0,len(m[0])):
        count = 0
        max_count = 0
        for j in range(0,len(m)):
            count = m[j][i]
            if(count>max_count):
                max_count = count

        new_list.append(max_count)        

    return new_list       



m = [[15,2,3],[4,5,6],[7,21,9],[10,11,12],[13,14,15]]

print(count_column_max(m))
		
		
    

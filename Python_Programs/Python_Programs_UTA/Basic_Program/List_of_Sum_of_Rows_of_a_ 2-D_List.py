

def row_sum_list(m):
    new_list = []
    for i in m:
        new_list.append(sum(i))

    return new_list


m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

print(row_sum_list(m))

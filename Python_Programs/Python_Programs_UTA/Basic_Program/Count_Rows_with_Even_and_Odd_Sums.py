
def count_rows_evensum_oddsums(m):
    even_count = 0
    odd_count = 0

    for row in m:
        row_sum = sum(row)
        if row_sum %2 == 0:
            even_count = even_count + 1
            
        else:
            odd_count = odd_count + 1


    print("even_count = ", even_count)
    print("odd_count = ", odd_count)
     

m = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

count_rows_evensum_oddsums(m)

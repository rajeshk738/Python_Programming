def rows_sorted(_2d_list):
    for rows in _2d_list:
        rows.sort(reverse=True)
    return _2d_list    



m = [[15,2,3],[4,5,6],[7,21,9],[10,11,12],[13,14,15]]

print(rows_sorted(m))

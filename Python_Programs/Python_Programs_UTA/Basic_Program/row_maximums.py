
def row_maximums(a):
    dict = {}
    s1 = "row "
    s2 = " max"
    i = 0
    for row in a:
        maximum = max(row)
        string = s1+str(i)+s2
        i = i + 1
        dict[string] = maximum

    return dict


a = [[5, 0, 0, 0, 13],
 [0, 12, 0, 0],
 [20, 0, 11, 0],
  [6, 0, 0, 8]]


print(row_maximums(a))
        
        
    
        


def one_to_2D(sample_list, r, c):
    list_2d = []
    sample_list = sample_list[:r*c]    
    x = 0
    y = c
    for i in range(0,r):
        list_2d.append(sample_list[x:y])
        x = c
        y = x + c
    return list_2d



print(one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 3, 3))

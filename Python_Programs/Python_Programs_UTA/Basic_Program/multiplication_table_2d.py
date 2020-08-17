def multiplication_table(n):
    output_list = []
    k = 0
    for i in range(0,n):
        k = k + 1
        sample_list = []
        for j in range(1,n+1):
            sample_list.append(j*k)

        output_list.append(sample_list)
        

    return output_list





print(multiplication_table(5))

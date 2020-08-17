def _recursive_sum_sample_(sample_list):
    my_sum = 0
    for element in sample_list:
        if type(element) != type([]):
            my_sum += element
        else :
            my_sum += _recursive_sum_sample_(element)
    return my_sum


nested_list = [1, -1, [2, -2], [3, -3, [4, -4], 10,20]]

print(_recursive_sum_sample_(nested_list))
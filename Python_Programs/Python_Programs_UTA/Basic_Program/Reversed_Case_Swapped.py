
def reverse_string(s):
    sample_list = list(s)
    sample_list.reverse()
    str = ""
    for i in range(0,len(sample_list)):
        sample_list[i] = sample_list[i].swapcase()
    str = str.join(sample_list)
    
    return str

input_string = 'Graphics is a great class to take'
print(reverse_string(input_string))

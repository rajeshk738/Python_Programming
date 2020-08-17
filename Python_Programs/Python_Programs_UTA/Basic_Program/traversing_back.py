
def traversing_backwards(input_list):
    length = len(input_list)
    i = -1
    output_list = []
    while(i >= -length):
        output_list.append(input_list[i])
        i = i - 1
    return output_list

input_list = ['apples', 'eat', "don't", 'I', 'but', 'Grapes', 'Love', 'I']

print(traversing_backwards(input_list))




def unique(input_list1,input_list2):
    output_list = []
    for items in input_list1:
        if items not in output_list:
            output_list.append(items)

    for items1 in input_list2:
         if items1 not in output_list:
             output_list.append(items1)

    return output_list


a = [1,2,2,5,4,4,5,3]
b = [1,2,3,4,5,6]

print(unique(a,b))

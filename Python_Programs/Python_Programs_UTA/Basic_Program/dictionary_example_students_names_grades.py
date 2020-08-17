
def fun(dict):
    output_list = []
    keys = dict.keys()

    for k in keys:
        grade1 = dict[k][0]
        grade2 = dict[k][1]
        grade3 = dict[k][2]

        if grade1 >= 75 and grade2 >= 75 and grade3 >= 75:
            output_list.append(k)

    return output_list

dict = {'rajesh':[75,78,85],'ram':[70,75,85],'lok':[78,95,88]}
print(fun(dict))

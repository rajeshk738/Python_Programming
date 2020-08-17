"""
file data:

Lucas,Turing,22
Alan,Williams,27
Layla,Trinh,21
Brayden,Huang,22
Oliver,Greek,20


then your function should return a list such as

['Lucas,Turing,22', 'Alan,Williams,27', 'Layla,Trinh,21', 'Brayden,Huang,22', 'Oliver,Greek,20']

"""

def file_list(file_name):
    f = open(file_name,"r")
    output_list = []
    data = f.readlines()

    for line in data:
        stripped_line = line.strip('\n')
        output_list.append(stripped_line)

    return output_list

print(file_list("E:\\test1.txt"))



"""

Write a function that accepts a filename as input argument,
the file contains the information about a persons expenses on milk and
bread and returns a dictionary that contains exactly the strings 'milk' and
'bread' as the keys and their floating point values in a list as values.
Each line of the file may start with a 'm' or a 'b' denoting
milk or bread respectively.
For example if the contents of the file are:

m 0 0 0
b 2 5 1
b 3 5 4
m 1 0 0
b 5 3 1
m 0 1 0
b 2 4 5

then your function should return a dictionary such as:

out_dict = {'milk': [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], 
            'bread': [[2.0, 5.0, 1.0], [3.0, 5.0, 4.0], [5.0, 3.0, 1.0], [2.0, 4.0, 5.0]]}




"""

def _construct_nested_list_from_file_sample_(filename):
    my_dictionary = {}
    my_dictionary["milk"] = []
    my_dictionary["bread"] = []
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        first_character = line[0]
        if first_character == "m":
            # remove the first character
            # strip and split by white space
            vertex = line[1::].strip().split()
            # change the string items into floats
            vertex = [float(x) for x in vertex]
            my_dictionary["milk"] += [vertex]

        if first_character == "b":
            face = line[1::].strip().split()
            face = [float(x) for x in face]
            my_dictionary["bread"] += [face]
    return my_dictionary

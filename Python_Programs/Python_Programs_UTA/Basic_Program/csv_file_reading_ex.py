"""

a CSV file which contains the information about student's names and
their grades for four courses and returns a dictionary that contains
information about the students whose grades in both Math and
Chemistry is above 70.
Note that if the file has any comments (lines starting with #)
then you should ignore such a line. The file will have the following format:

#first_name,math,physics,chemistry,biology

For example if the contents of the file are:

Luke,89,94,81,97
Eva,40,50,65,90
Joseph,55,58,54,99
Oliver,73,74,89,91

then your function should return a dictionary such as:

out_dict = {'Luke': [89.0, 94.0, 81.0, 97.0],
            'Oliver': [73.0, 74.0, 89.0, 91.0]}



 """           








def _construct_dictionary_from_file_sample2_(filename):
    my_dictionary = {}
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        # Skip any lines that start with #
        if line[0] != '#':
            # Split the line with the delimiter comma (',')
            name, math, physics, chemistry, biology = line.strip().split(',')
            if float(math) > 70 and float(chemistry) > 70:
                my_dictionary[name] = [float(math), float(physics), float(chemistry), float(biology)]
    return my_dictionary


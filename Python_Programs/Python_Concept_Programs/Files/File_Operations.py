""" file data

Man: Is this the right room for an argument?
other Man: I've told you once.
Man: No you haven't!
other Man: Yes I have.
Man: When?
other Man: Just now.
Man: No you didn't!

"""

file = open("E:\\python.txt")
print("first line= ",file.readline()) # reads the line of the file and file pointer is set at end of the line             



file.seek(0)  # sets the file pointer to position 0
print("splitting the file data\n ")
for each_line in file:
    if(not each_line.find(':') == -1 ):          # If there is no colon in the line
        (role,line_spoken) = each_line.split(":")
        print(role,end='')
        print(' said: ',end='')
        print(line_spoken, end='')
   
file.close()    
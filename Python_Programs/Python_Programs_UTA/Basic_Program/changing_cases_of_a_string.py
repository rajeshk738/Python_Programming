"""
all the uppercase characters are changed to lower case
and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed.
Do NOT use the string methods upper(), lower(), or swap().

"""

def changing_case_of_string(string):
    outputstring = ""
    length = len(string)

    for i in range(0,length):
        x = ord(string[i])
        if(x > 96 and x < 123 ):
            outputstring = outputstring+chr(x-32)
        elif (x>64 and x < 91):
            outputstring = outputstring+chr(x+32)

    return outputstring


print(changing_case_of_string("rAjEsh"))

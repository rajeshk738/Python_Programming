 
################### Sample Solution ###################
"""
 For example if the input is 4721 then the function should return
 the string "four seven two one".

 """

def words(sample_integer):
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"1" : "one",
                         "2" : "two",
                         "3" : "three",
                         "4" : "four",
                         "5" : "five",
                         "6" : "six",
                         "7" : "seven",
                         "8" : "eight",
                         "9" : "nine",
                         "0" : "zero"}
    output_string = ""
    for integer in splitted:
        output_string += sample_dictionary[integer] + " "
    # remove any trailing whitespace
    stripped = output_string.rstrip(" ")
    return stripped


print(words(4521))

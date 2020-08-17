# This function accepts a string as input
# and returns the reverse of the input string

def reverse_string(input_str):
    output_str = ""

    for char in input_str:
        output_str = char + output_str

    return output_str


test = "Hello"
result = reverse_string(test)
print(result)

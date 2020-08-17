"""
4 digit integer (from 1000 to 9999 both inclusive)

Sample Examples:
if the input integer is 7000 then the function should return the string "seven thousand"
if the input integer is 1008 then the function should return the string "one thousand eight"
if the input integer is 4010 then the function should return the string "four thousand ten"
if the input integer is 1012 then the function should return the string "one thousand twelve"
if the input integer is 4506 then the function should return the string "four thousand five hundred six"
if the input integer is 9900 then the function should return the string "nine thousand nine hundred"
if the input integer is 8880 then the function should return the string "eight thousand eight hundred eighty"
if the input integer is 5432 then the function should return the string "five thousand four hundred thirty two"


"""

def Numbers_to_words(n):
    output_string = ""
    dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty',
90:'ninety', 100:'hundred', 1000:'thousand'}

    number_digit = list(str(n))
    fourth_digit = int(number_digit[0])
    third_digit = int(number_digit[1])
    second_digit = int(number_digit[2])
    first_digit = int(number_digit[3])

    if(fourth_digit != 0):
        output_string = dict[fourth_digit]+" "+dict[1000]
        if(third_digit == 0 and second_digit == 0 and first_digit == 0):
            return output_string

    if(third_digit != 0 ):
        output_string = output_string+" "+dict[third_digit]+" "+dict[100]
        if(second_digit == 0 and first_digit ==0):
            return output_string

    if(second_digit == 0 and first_digit != 0):
        output_string = output_string+" "+dict[first_digit]
        return output_string
    
    if(first_digit == 0 and second_digit != 0):
        second_digit = second_digit * 10
        output_string = output_string+" "+dict[second_digit]
        return output_string
    if(first_digit != 0 and second_digit != 0):
        if(second_digit == 1):
            second_digit = 10 + first_digit
            output_string = output_string+" "+dict[second_digit]
            return output_string
        else:
            output_string = output_string+" "+dict[second_digit*10]+" "+dict[first_digit]
            return output_string
        
    
        

print(Numbers_to_words(7000))
print(Numbers_to_words(1008))
print(Numbers_to_words(4010))
print(Numbers_to_words(1012))
print(Numbers_to_words(4506))
print(Numbers_to_words(9900))
print(Numbers_to_words(8880))
print(Numbers_to_words(5432))
print(Numbers_to_words(4521))  

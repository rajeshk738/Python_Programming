

def palindrome_string_check(string):
    if(string[::].lower() == string[::-1].lower()):
        return True
    else:
        return False



if(palindrome_string_check("amma")):
    print("palindrome")

else:
    print("not palindrome")

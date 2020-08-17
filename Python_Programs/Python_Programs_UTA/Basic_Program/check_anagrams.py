

def anagrams_check(sample_string1, sample_string2):
    if sorted(sample_string1.lower()) == sorted(sample_string2.lower()):
        return True
    else:
        return False



s1 = "rajesh"
s2 = "ajrhes"

if(anagrams_check(s1,s2)):
    print("given strings are anagrams")
else:
    print("not anagrams")
    

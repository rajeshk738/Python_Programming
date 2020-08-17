
def most_common_character(s):
    s = s.lower()
    sample_string = s.replace(" ", "")
    length = len(sample_string)
    set_max_count = 0
    set_char = ' '
    count = 0
    for char in sample_string:
        count = sample_string.count(char)

        if(count >= set_max_count):
            set_max_count = count
            set_char = char
            
    print(set_char)
    print(set_max_count)


s = "ya gotta make do with what ya got"
     
most_common_character(s)       

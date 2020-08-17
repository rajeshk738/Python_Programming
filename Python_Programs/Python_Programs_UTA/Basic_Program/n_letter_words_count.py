# This funtion finds the number of n letter words
# in the input string

def find_n_letter_words(input_str,n):
    words = input_str.split()
    print(words)
    n_letter_words = 0
    
    for word in words:
        if len(word) == n:
            print(word)
            n_letter_words = n_letter_words + 1

    return n_letter_words


test_str = "He who would learn to fly one day"
print(find_n_letter_words(test_str,2))
        

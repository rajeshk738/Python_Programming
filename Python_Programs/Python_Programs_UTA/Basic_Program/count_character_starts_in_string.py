def count_words(string,c):
    my_list = string.split()
    c = c.lower()
    length = len(my_list)
    count = 0
    for str in range(0,length):
        if (my_list[str].lower().startswith(c) == True):
            count = count + 1

    return count


print(count_words("hi ra rajesh How are you r h H  h h hmm?",'H'))

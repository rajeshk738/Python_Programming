def _remove_leading_whitespace_sample_(string):
    my_index = None
    for x in range(0, len(string)):
        if string[x] != " ":
            my_index = x
            break
    # slice the string from that index to the end
    new_string = string[my_index::]
    return new_string


print(_remove_leading_whitespace_sample_("    hello    "))

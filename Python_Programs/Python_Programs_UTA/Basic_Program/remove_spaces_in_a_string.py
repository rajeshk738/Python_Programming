def remove_spaces(string):
    out_string = ""
    for x in range(0, len(string)):
        if string[x] != " ":
            out_string = out_string + string[x]
    return out_string

print(remove_spaces(" ra jesh !"))

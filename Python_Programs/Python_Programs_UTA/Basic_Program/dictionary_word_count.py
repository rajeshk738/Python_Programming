
def dictionary_word_count(s):
    dict = {}
    string_list = s.lower().split()
    for words in string_list:
        dict[words] = string_list.count(words)

    return dict



s = "I am tall when I am young and I am short when I am old"

print(dictionary_word_count(s))



def count_vowels_string(s):
    s = s.lower()
    count = 0
    vowels = list("aeiou")
    for char in range(0,len(s)):
        if s[char] in vowels:
            count = count +1

    return count


print(count_vowels_string("rajesh"))

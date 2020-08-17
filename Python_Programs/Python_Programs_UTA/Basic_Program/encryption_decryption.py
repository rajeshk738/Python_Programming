
def encrypt(a):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    character_list = list(character_set)
    secret_list = list(secret_key)

    a_list = list(a)
    length = len(a_list)

    for i in range(0,length):
        index = character_list.index(a_list[i])
        a_list[i] = secret_list[index]

    s = ""
    a = s.join(a_list)
    return a


a = "Lets meet at the usual place at 9 am"

print(encrypt(a))


"""

def _encryption_sample_ed2_0215(my_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted_message = ""
    for character in my_string:
        index = character_set.find(character)
        encrypted_message = encrypted_message + secret_key[index] 
  
    return encrypted_message
"""
    
    

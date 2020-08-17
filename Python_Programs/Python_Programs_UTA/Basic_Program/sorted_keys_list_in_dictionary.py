# sorted keys list in dictionary

def sorted_keys(a):
    keys = a.keys() 
    keys = list(keys)  # change dictionary view to list
    keys.sort()
    return keys

"""

def sorted_keys(a):
    keys = sorted(a)
    return keys
    
"""

dict = {1:5,8:2,5:4,6:7,3:5}

print(sorted_keys(dict))
    


def duplicate(a):
    b = []

    for i in a:
        if i not in b:
            b.append(i)
    return b

a = [2,3,4,2,5,3,6,4,1]
print(duplicate(a))

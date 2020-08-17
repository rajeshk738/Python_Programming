cast = ["Cleese","Palin",'Jone','Idle']

# addding at the end
cast.append("Galliwan")
print(cast)

# inserting element at specified position

cast.insert(0,"rajesh")
print(cast)

# removing specified element

cast.remove("rajesh")
print(cast)

# pop out the element at specified index value
cast.pop()  #last item
print(cast)

cast.pop(1)
print(cast)

# extending the list
cast.extend(["rajesh","ramesh"])
print(cast)

# length of the list

print(len(cast))

# type check

print(type(cast))

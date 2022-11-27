# tuples - stores multiple items in a single variable
# non-homogeneous
# ordered
# unchangable/immutable
# allows duplicate values




# myTuple = (1,2,3,4,4)
# print(len(myTuple))
# print(myTuple)

# tuple1 = ("apple",1,1.1)
# print(tuple1)

# tuple1 = ("car","bike","boat","jet")
# print(tuple1[:4])

tuple1 = ("car","bike","boat","jet")
list1 = list(tuple1)
list1.append("drone")
tuple= tuple(list1)
print(tuple)

# we call () as paranthesis
tuple1 = (10,20,30,40)
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i+=1

# tuple1 = (10,20,30,40)

# for i in tuple1:
#     print(i)

tuple1 = (10,20,30,40)
list1 = list(tuple1)
list2 = list1.copy()
tuple2 = tuple(list2)
print(tuple2)


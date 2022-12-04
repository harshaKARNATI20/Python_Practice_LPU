# set - store multiple values in single variable
# unordered




# mySet = {"car","boat","train"}
# print(mySet)
# if "boat" in mySet:
#     print("boat")

# unchangable / immutable
# duplicates not allowed
# non-homogeneous

# tuple1 = ("H","E","L","L","O")
#output - HELLO
# for i in tuple1:
    # print(i,end="")


mySet1 = {"car","boat","train"}
mySet2 = {1,2,3}
mySet1.add("cycle")
mySet1.update(mySet2)

print(mySet1)

mySet1 = {"car","boat","train"}
mySet2 = {1,2,3,4}
mySet3 = {4,5,6,7}

output = mySet2.union(mySet3)
print(output)

mySet1 = {"car","boat","train"}
mySet2 = {1,2,3,4}
mySet3 = {4,5,6,7}
output1 = mySet2.intersection(mySet3)
print(output1)
output2 = mySet2.symmetric_difference(mySet3)
print(output2)

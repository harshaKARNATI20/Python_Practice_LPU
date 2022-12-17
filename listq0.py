# Question1:
#  triple all the elements in the list
# list1 = [10,20,30,40,50]

# output1=list(map(lambda i:i*3,list1))
# print(output1)

# Question2:
# Print out all the multiples of 5 using filter and lambda
list2 = [34,88,30,22,10,15,18]

output2=list(filter(lambda i:i%5==0,list2))
print(output2)
# list1 = [3,2,8,16,11,34,17]
# output = list(filter(lambda i : i>15,list1))
# print(output)

n=int(input("Enter the Number: "))
count=2
while count*count<n:
    if n%count==0:
        print("NotPrime")
    else:
        print("Prime")
    count+=1
list1 = [3,2,8,16,11,34,17]
output1 = list(map(lambda i: i+2,list1))
output2 = list(map(lambda i: i**2,list1))
print(output1)
print(output2)
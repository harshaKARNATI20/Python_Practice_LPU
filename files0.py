# Like notes,we can create and access files using python
f = open("demo.txt","r")
# print(f.read()),This reads a file i.e., prints the data in the text file
# print(f.readline())
# print(f.readline())
# The file should be in the same directory,but not in the same folder

# with open("demo.txt") as f:
    # f.read() #--> example
    # your code goes here

print(f.read(10))
print(f.tell())

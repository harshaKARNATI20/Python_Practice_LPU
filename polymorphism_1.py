a = "Hello"
b = [1,2,3,4,5,6]

print(len(b))
print(len(a))

# Here,the length is used for a string and for a list
# As it is working of many forms,This phenomena is called polymorphism

def add(a,b,c = 0):
    return a+b+c

print(add(1,2))
print(add(1,2,3))
# this is called method overloading
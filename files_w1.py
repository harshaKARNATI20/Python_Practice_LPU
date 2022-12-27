f = open("demo.txt","r")
a = open("demo3.txt","w")
a.write("This is a new file\n")
a.write("This is a random Text\n")
a.write("This is a file\n")

for i in f:
    print (i)

# # create a function using following conditions
# # It should accept employee name and salary and display both

# # if the salary is missing in the function then assign the default value 10000 to salary
# #Ben(9000)   mike(15000) Bob()

# def Employee(name,salary=10000):
#     print("Name: "+ name,"Salary: ",salary)

# Employee("Ben",9000)
# Employee("mike",15000)
# Employee("Bob")

# def info(name, **data):
#     print(name)
#     print(data)

# info("Harsha",age = 19, place = "West Godavari", num = 8184883230)

def info(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

info("Harsha",age = 19, place = "West Godavari", num = 8184883230)
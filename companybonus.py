import time


timeSpent = int(input("Enter the time" ))
salary = float(input("Enter the salary"))

if timeSpent > 10:
    print("The bonus amount is :",salary+(salary)*0.1)
elif timeSpent > 6 and timeSpent < 10:
    print("The bonus amount is :", salary+(salary)*0.08) 
elif timeSpent < 6:
    print("The bonus amount is :", salary+(salary)*0.05)
else:
    print("Invalid data")


totalClasses = int(input("Enter the classes"))
classesAttended = float(input("enter"))

attendance = (classesAttended / totalClasses) * 100


if(totalClasses == classesAttended):
    print("The attendance is 100%")

else:
    print(attendance)
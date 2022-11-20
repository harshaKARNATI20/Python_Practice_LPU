#list can print different types like strings,integers,floats etc..,
#lists are ordered # can print duplicate values 
# list is denoted by [] whereas tuple is denoted by ()
colors = ["Red","Blue","Black","Red",22]
cars = ["AUDI","MERC","LAMBO","FERRARI"]
players = ("Dhoni","Messi","Ronaldo","Kohli")

# colors[0:2] = ["Yellow" , "Orange"]

# colors[2] = "Green"
# print(colors[1:4])
# Insert will add a specified element at a certain position in the list
# colors.insert(2,"Indigo")
#append will add the element at last
# colors.append("BMW")

# colors.extend(cars)
# "remove" removes a specific element
# colors.remove("Red")
# pop removes from a specific index
# colors.pop(1)
# del deletes an element using its index
del colors[0]
colors.clear()
print(colors)

#"tuple' objects does not support item assignment"
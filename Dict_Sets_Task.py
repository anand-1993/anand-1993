# Define dictionary with float , int , list and tuple.
Dict = {"float" : 10.23, "int" : 45, "List" : ["Anand", "Som", 28], "tuple": ("Python", "Lang", "AWS")}
print(Dict)

# find the symmetric difference between followoing set
firstSet = { 1, 2, 3,5}
secondSet = { 1, 2, 3,4}
x = firstSet.symmetric_difference(secondSet)
print(x)

# Find the union on the two sets using or operator.
firstSet = { 1, 2, 3,5}
secondSet = { 1, 2, 3,4}
print(firstSet | secondSet)

# Find the common element between two sets using and operator
firstSet = {1,2,3,5}
secondSet = {1,2,3,4}
print( firstSet & secondSet)

# Find the different in set using minus operator
firstSet = { 1, 2, 3,5}
secondSet = { 1, 2, 3,4}
print( firstSet - secondSet)

# print the name value from following dictionary
dict1 = { "name" : "1", "age" :"3"}
print(dict1["name"])

# Update following dictionary with place an key and value as Akl
dict2 = { "name" : "1", "age" :"3"}
dict2["place"] = "Akl"
print(dict2)

# Update following dictionary with students an key and [{ "name" :"p1"}]
dict3 = { "name" : "1", "age" :"3"}
dict3.update({"name" : "p1"})
print(dict3)

# Print only keys from following dictionary
dict4 = { "name" : "1", "age" :"3"}
print(dict4.keys())

# Print only valyes from following dictionary
print(dict4.values())

# Create dictionary using fromkeys method.
test = ("test","test1")
value = "1"
dict5 = dict.fromkeys(test, 1)
print(dict5)

# Remove name from following dictionary
dict4 = { "name" : "1", "age" :"3"}
dict4.pop("name")
print(dict4)

# Define dictionary with list and update that list using append method.
diction = {"List" : ["computer", " Keyboard", "Mouse"]}
diction["List"].append("Monitor")
print(diction)
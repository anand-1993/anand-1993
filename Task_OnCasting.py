# Write program to convert tuple to list
print("Write program to convert tuple to list")
tupleData = (1,2,3,4,5)
list = [tupleData]
print(list)

# Write program to convert int to float, str to int
print("Write program to convert int to float, str to int")
x = 10
y = 145.23
z = "4"
print(float(x), int(z))

# Print last element from tuple using negative index
print(tupleData[-1])

# Print first element from tuple using negative index and positive index
print(tupleData[-len(tupleData)], tupleData[0])

# find the position of 1 element
for i in range(len(tupleData)):
    if tupleData[i]==1:
        print("1 element positin is", i+1)

# find the position of 5 element
for i in range(len(tupleData)):
    if tupleData[i]==5:
        print("1 element positin is", i+1)

# Print tuple in reverse Order
print(tupleData[::-1])

# Concate tuple using + operator.
tupleData = (1,2,3,4,5)
tupleData = (1,2,3,4,5)
print( tupleData + tupleData)

# Write program to declare variable with explit type and implict type.
varExplicit = int(20)
varImplicit = 20
print(varExplicit, varImplicit)

# write program to define None Type variables.
varNone = None
print(varNone)
# Take multiple inputs from Use
# x, y = input("Enter a two value: ").split()
#
# print(x)
# print(y)

# print(int(x) + int(y))
x = int(10)
y = float(10.10)
z = float(10.10)

x1, y2, tupleType,listType = "Orange", 10, (1,2,3,4,5),[1,2,3,4]

print(x1)
print(y2)
print(tupleType)
print(listType)

print("Second type of assigment or initlization")
x2, x3, tupleType1,listType2 = "Orange", 10, (1,2),list()

listType2.append(10)
print(x2)
print(x3)
print(tupleType1)
print(listType2)
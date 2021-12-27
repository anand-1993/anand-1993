# Remove element from sets.
firstSet = {1,2,3 }
firstSet.remove(1)
print(firstSet)

# Find the difference between two sets
firstSet = {1,2,3 }
SecondSet = {1,2,3,4 }
x = firstSet.difference(SecondSet)
y = SecondSet.difference(firstSet)
print(x)
print(y)

# Define multiple dimention list add element to it
MulList = [["Python", "Lang", 100],["Java", "Lang1", 200],["aws", "cloud", 300]]
print(MulList)

# Define multiple dimention tuple add element to it
MulTuple = (("Python", "Lang", 100),("Java", "Lang1", 200),("AWS", "Cloud", 300))
print(MulTuple)

# Find the common elemnt from following sets
firstSet = {1,2,3 }
SecondSet = {1,2,3,4 }
x = SecondSet.intersection(firstSet)
print(x)

# Update the first and secondtuple.
firstSet = {1,2,3}
Secondtuple = (1,2,3,4)
firstSet.add(5)
x = list(Secondtuple)
x.append(6)
Secondtuple = tuple(x)
print(firstSet)
print(x)

# Find the common element from sets and update it with list
firstSet = {1,2,3}
SecondSet = {1,2,3,4}
thirdSet = {1,2,3,4,5}
x = SecondSet.intersection(firstSet)
y = thirdSet.intersection(x)
c = list(y)
print(c)

# Remove 1 element from all sets of list
firstSet = {1,2,3 }
SecondSet = {1,2,3,4 }
thirdSet = [1,2,3,4,5 ]
x = list(firstSet)
y = list(SecondSet)
z = list(thirdSet)
x.remove(1)
y.remove(1)
z.remove(1)
firstSet = set(x)
SecondSet= set(y)
thirdSet = set(z)
print(firstSet, SecondSet, thirdSet )

# Create the copy of all sets and update with list and remove 5 element from sets.
firstSet = {1,2,3 }
SecondSet = {1,2,3,4 }
thirdSet = [1,2,3,4,5 ]
firstSet.update(SecondSet)
firstSet.update(thirdSet)
list1 = list(firstSet)
list1.remove(5)
firstSet = set(list1)
print(firstSet)

# Access the list using for loop.
firstSet = {1,2,3 }
list2 = list(firstSet)
for i in list2:
    print(i)
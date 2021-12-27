# Define two variable x = 10 and y = 20
# check x number is positive and 20 is positive number using and
x = 10
y = 20
print(x and y > 0)

#Define two variable x = 10 and y = 20
#check x number is negative and 20 is negative number using or
print( (x or y) < 0)

# Define two variable x = 10 and x = 20
# check x is number positive or grater than 0 using or operators.
print((x or y) > 0)

# Find the first element and last element from below list and check those numbers grater than 0
list1 = [1,2,3,4,5,6]
print((list1[1] or list1[-1]) > 0)

# Find the 2 element and 4 element from above list and check those numbers grater than 0
index = int
index1 = int
for i in list1:
    if i == 2:
        index = i
    else:
        if i == 4:
            index1 = i
print((list1[index] and list1[index1]) > 0)

# Define above two list find 1 element from first list and from second list.
# Check both number are positive or not
list1, list2 = [1,2,3,4,5,6] ,[1,2,3,4,5,6]
for i in list1:
    if i == 1:
        break
for x in list2:
    if x==1:
        break
print(( i and x) > 0)






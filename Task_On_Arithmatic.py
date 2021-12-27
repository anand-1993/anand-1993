# Define 2 variable with value 40 and 50 , use the == operator and print both values are not equal
x = 50
y = 40
print(" are both equal : ", x == y)

# Define 2 variable with value 110 and 110 , use the == operator and print both values are equal
x = 110
y = 110
print(" are both equal : ", x == y)

# Define two list with value [1,2,3,4,5] and [6,7,8,9,10] use negative index find last element from both
# and use != operator to check last elemetn is same or different
lis1, list2 = [1,2,3,4,5], [6,7,8,9,10]
print("are Last elements not  equal : ", lis1[-1] != list2[-1])

# Define two list with values [1,2,3,4,5] and [6,7,8,9,10] use positive index find last element from both list
# Check last element is smaller or grater
print("Last element in list1 is greater:" ,lis1[len(lis1)-1] > list2[len(list2)-1])
print("last element in list2 is greater:" ,lis1[len(lis1)-1] < list2[len(list2)-1])

# Define two list with values (1,2,3,4,5) and (6,7,8,9,10) use positive index find last element from both list
# Check last element is equal or not
print("are both equal:" ,lis1[len(lis1)-1] == list2[len(list2)-1])

# Define integer with value 10,100 and do addition,substraction, multiplication and division
x = 10
y = 100
print("Addition is ", x + y, "\nMultiplication is ", x * y, "\n Substaction is ", y - x, "\nDivision is ", y/100)

# Define two variable 133, 20 and find the reminder
x = 133
y = 20
print( 133 % 20)

# Define two variable and find out element is grater than or equal and less than equal.
x = 20
y = 10
if x >= y:
    print("Yes it is greate or equal ")
else:
    print("yes it is less or equal")



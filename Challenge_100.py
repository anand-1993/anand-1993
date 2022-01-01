# 1) Python program to reverse a number with explanation
x = input("Enter Number ")
print(x[::-1]) #  taking input as string  array we can print all digit using index position in array, in python
# we can print input in reverse order by putting range in index within square  bracket [ ].
# using logic
z = input("Enter Digit ")
y = int(z)
reverse = 0
digit = 0
while y != 0: # here we are taking some calculation under while loop till condition is satisfied ,
    digit = y % 10 # mod (%) operator return reminder tp  variable.
    reverse = reverse * 10 + digit # after getting reminder , we are multiplying 10 to add upcoming digit.
    y = int(y / 10) # this return left most digits except last digit.
print(reverse) # finally printing all digit in reverse order.

# 2) Armstrong number program in python with explanation
#An Armstrong number, also known as narcissistic number, is a number that is equal to the sum of the cubes of its own digits.
#For example, 370 is an Armstrong number since 370 = 3*3*3 + 7*7*7 + 0*0*0
x = int(input("Enter Number "))
z = 0
sum = 0
y = int(x)
while y != 0:
    z = y % 10
    sum += z*z*z
    y = int(y / 10)
if x == sum:
    print("Yes it is Armstrong Number")
else:
    print("No it is not armstrong Number")

# 3) Prime number program in python with explanation
print("Enter Number to check if it prime or not")
flag = False
y = int(input())
for i in range(2, y):
    if y % i == 0:
        flag = True
        break
if flag:
    print("Not Prime")
else:
    print("It's Prime")
    
# Another Logic
print("Enter Number")
y = int(input())
flag = False
z = int((y-3)/2)
count = int(1)
if y == 2:
    print("It is Even Prime Number")
elif y != 2 and y % 2 == 0:
    print("It is not Prime")
else:
    for i in range(z):
        if y % int(count + 2) == 0:
            flag = True
            break
        else:
            count += 2
    if flag:
        print("It is not prime")
    else:
        print("yes it is prime")

# 4) Fibonacci series program in python using iterative method
x = int(input("Enter Number to find its Fibonacci "))
pre, next = 0, 1
for i in range(x):
        temp = pre  + next
        pre = next
        next = temp
print(pre)

# 5) Write a program in Python to check whether a number is palindrome or not using iterative method.
x = input("Enter Number ")
rev = 0
z = int(x)
for i in x:
        y = z % 10
        rev = (rev * 10) + y
        z = int(z/10)

if rev == int(x):
        print("it's Palindrome")
else:
        print("It's not Palindrome")

# 6) Write a program in Python to find greatest among three integers.
list = []
x = input("Enter Three Numbers ").split()
for i in x:
        list.append(int(i))
print(list)
if list[0] > list[1] and list[2]:
        print(list[0], "is Greatest ")
elif list[1] > list[2]:
        print(list[2], "is Greatest")
else:
        print(list[2], "is Greatest")

# 7) Python program to swap two number without using third variable
x = int(input("Enter value of X =  "))
y = int(input("ENter Value of Y =  "))
print("Befor Swap \nX =",x,"Y =", y)
x = x + y
y = x - y
x = x - y
print("After swap \nX =",x, "Y =",y)

# 8) Python Program to swap two number using third variable
x = int(input("Enter value of X =  "))
y = int(input("ENter Value of Y =  "))
print("Befor Swap \nX =",x,"Y =", y)
temp = int
temp = x + y
x = temp - x
y = temp - y
print("After swap \nX =",x, "Y =",y)

# 9) Perfect number program in Python with example
x = int(input("Enter Number to check it is perfect or not  "))
sum = 1
for i in range(2,x):
       if x % i == 0:
               sum += i
if sum == x:
        print("It's Perfect Number")
else:
        print("No It's Not Perfect number")

# 10) add two numbers without using addition operator
print("Enter Two Values Seperate using space")
x = input().split(" ")
y =[]
for i in x:
    y.append(int(i))
print("Addition =", sum(y))
# 11) Python program to remove character from string
x = input("Enter String ")
print("Entr character to remove from the string")
y = input()
new = ""
list = []
for i in x:
        list.append(i)
for i in list:
        if i == y:
                continue
        else:
                new = new + i
print("after Removal")
print(new)

#  12 Write program to check string is Anagram
x = input("Enter String ")
y = input("Enter String ")
l1, l2 = [],[]
if len(x) == len(y):
    for i in x:
        l1.append(i)
    for i in y:
        l2.append(i)
print(l1.sort() == l2.sort())

# 13) String Palindrome program in python
# 1st way
x = input("Enter String ")
for i in x:
    new = x[::-1]
print(x == new)
# 2nd way
new1 = ""
len = len(x)
while len >=1:
    new1 = new1 + x[len-1]
    len -= 1
print( x == new)

# 14) Python Program to remove duplicates from Array
x = input("Enter data ").split(" ")
x = list(set(x))
print(x)

# 15) Python Program to find sum of array
# 1st way
x = input("Enter Numbers ")
l1 = []
for i in x:
    l1.append(int(i))
print("Sum is",sum(l1))

# 2nd way
k = input("Enter Number ")
m = 0
for i in k:
    m = m + int(i)
print("Sum is", m)

# 16) Remove duplicate numbers from list [1,1,1,3,3,4]
li = [1,1,1,3,3,4]
li = set(li)
l2 = []
for i in li:
    l2.append(i)
print(l2)

# 17) do sum of all numbers in list [4,4,5,6,6,7,7,7,7,7,7,101]
# 1st way
list = [4,4,5,6,6,7,7,7,7,7,7,101]
print(sum(list))
# 2nd way
sum = 0
for i in list:
    sum =sum + i
print(sum)

# 18) Find Event Number from List [2,3,4,1,4,5,7,8]
List = [2,3,4,1,4,5,7,8]
new = []
for i in List:
    if int(i) % 2 == 0:
        new.append(i)
print(new)

# 19) Sort following list :
# my_list = [5, 2, 90, 24, 10]
my_list = [5, 2, 90, 24, 10]
my_list.sort()
print(my_list)

# 20) 20 make SUM of all values which has same value
# { "one" : "1", "two" : "2","three" : "2","four" : "1","five" : "1"}
dict = { "one" : "1", "two" : "2" ,"three" : "2", "four" : "1" ,"five" : "1"}
count = 0
cnt = 0
for i in dict:
    if dict[i] == "1":
        count = count + int(dict[i])
    else:
        if dict[i] == "2":

            cnt = cnt + int(dict[i])
print("sum of whose value are 1 is ", count)
print("sum of whose value are 2 is ", cnt)


# 21) Find the difference between two list
# [1,2,3,4,5,7,8,8]
# [1,2,3,4,5,6,7]
Lst1 = [1,2,3,4,5,7,8,8]
Lst2 = [1,2,3,4,5,6,7]
Lst1 = set(Lst1)
Lst2 = set(Lst2)
y = Lst1.difference(Lst2)
print(y)

# 22) Reverse words in a given String in Python
# word = "python"
word = "python"
print(word[::-1])

# 23) Find following string contain specail character
# stringName ="$$Spcail Char"
#stringName ="$$Spcail Char"
print("Enter String With Special Characters")
stringName = input()
alpha = ""
flag1 =False
flag2 =False
speChr = ""
for i in stringName:
    for x in range(97, 123) :
        if x == ord(i):
            flag1 = True
            break
        else:
            for x in range(65, 91):
                if x == ord(i):
                    flag2 = True
                    break
    if flag1:
        flag1 = False
        alpha = alpha + i
    else:
        if flag2:
            flag2 = False
            alpha = alpha + chr(x)
for i in stringName:
    if i in alpha or i.isdigit():
        continue
    else:
        speChr = speChr + i
print("These are special characters ",speChr)

# 24) Convert numeric words to numbers. (Define dictionary and get the actual value)
# input ="on four two one"
print("Enter Numeric Words")
num = 0
x = input().split(" ")
dict1 = { "on" : 1, "four" : 4, "two" : 2, "one" : 1}
y = list(dict1.values())
z = list(dict1.keys())
if x == z:
    for i in y:
        num = num* 10  + i
    print(num)
else:
    print("Invalid Input")

# 25) Remove similar characters from string
# input = "pankaj"
# output = pnkj
count = 0
print("Enter String ")
new = ""
flag = False
x = input ()
for i in x:
    for z in x:
        if i == z:
            count = count + 1
            continue
        else:
            if count > 1:
                new = new + i
                break
    count = 0
new = set(new)
unique = ""
for i in x:
    if i in new:
        continue
    else:
        unique = unique + i
print(unique)

# 26)  Check string is subsubstring.
# stringValue = "python"
# substring = "py"
# output : true
substring = "py"
stringValue = "python"
print(substring in stringValue)

# 27) Reverse string using for loop
print("Enter String")
x = input()
new = ""
for i in reversed(x):
    new = new + i
print(new)

# 28) Add - instead of . into string
#  inputString = "p.y.t.h.o.n"
#  output : p-y-t-h-o-n
print("Enter String")
inputString = input()
inputString = inputString.replace("." , "-")
print(inputString)

# 29)  Find 'a' from following list
# ["a","b","c","d"]
arr = ["a","b","c","d"]
for i in arr:
   if  i == "a":
       break
print(i)

# 30)Remove duplicate "occurence" of the string
# inputString = "I M learning python , python is good language. python is dynamic language"
inputString = "I M learning python , python is good language. python is dynamic language.".split()
list1 = inputString
index = []
count = 0
set1 = set()
for i in range(len(list1)):
    for x in range(len(inputString)):
        if list1[i] == inputString[x]:
            count += 1
            if count > 1:
                set1.add(x)
    count = 0
new = ""
for i in range(len(inputString)):
    if i not in set1:
        new = new + " " + inputString[i]
        continue
print(new)

# 31) Define the dictionary of students with property Name, age. Create list of dictionary
#students = [ {"name" :"Sachin","age" : 20},{"name" :"pankaj","age": 30} ,{"name" :"Ajay","age": 10},
# ,{"name" :"Ajay2","age": 24}]

students = [{"name" :"Sachin","age" : 20},{"name" :"pankaj","age": 30} ,
            {"name" :"Ajay","age": 10   },{"name" :"Ajay2","age": 24}]
# Find the students who has 20 age
y = input("Search By age ")
y = int(y)
z = list()
flag = False
for b in students:
    for c in b:
        if c == "age":
            z.append(b[c])
            break

if y not in z:
    print("Age is not Exist in Dictionay")
else:
    for i in students:
        for x in i:
            if i[x] == y:
                flag = True
                break
        if flag:
            print(i)
            break
# Find the sudent who has more than 20
y = input("Search Student more than Age given by user ")
y = int(y)
flag = False
for i in students:
    for x in i:
        if x == "age" and i[x] > y:
            flag = True
            break
    if flag:
        flag = False
        print(i)
#Find the students who name is pankaj and age 30
flag = False
for i in students:
    for x in i:
        if i["name"] == "pankaj" and i["age"] == 30:
            flag = True
            break
    if flag:
        print(i)
        break   
#Sort the student by their age smaller to older
def sortDict(c):
  return c["age"]



students.sort(key=sortDict)
print(students)
#Find the student who has less or equal age than 10
flag = False
for i in students:
    for x in i:
        if x == "age":
            if i[x] <= 10:
                flag = True
                break
    if flag:
        flag = False
        print(i)

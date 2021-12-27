# Length of a string 1st way
print("Length of a string 1st way")
x = input("Enter String To know Its Length ")
print("Length of the string is", len(x))
print("Second way")
x = input("Enter String To know Length ")
count =0
for i in range(len(x)):
    count += 1
print("Length of the string is", count)


print("Take two strings from the input and print weather or not the strings are equal")
# Take two strings from the input and print weather or not the strings are equal
x = input("Enter Two String Compare ").split()
print(x[0]==x[1])


print("Take a string from the input and print the last character of that string")
# Take a string from the input and print the last character of that string
x = input("Enter String ")
print(x[-1])


print("Take a string from the input and check weather or not it contains both letters and numerals")
# Take a string from the input and check weather or not it contains both letters and numerals
x = input("Enter String ")
print(x.isalnum())

print("Take a string from the input and check all the letters in the string are of lower case")
# Take a string from the input and check all the letters in the string are of lower case
x = input("Enter String ")
print(x.islower())


print("Take a string from the input and print it in reverse")
# Take a string from the input and print it in reverse
x = input("Enter String ")
print("its reverse is", x[::-1])


# Take a string from the input and remove the vowels and print it
print("Take a string from the input and remove the vowels and print it")
x = input("Enter String ")
Vowels = "a e i o u A E I O U"
Temp = ""
for i in x:
    if i in Vowels:
        continue
    else:
        Temp = Temp + i
print(Temp)

# Take a string from the input and print ascii character
print("Take a string from the input and print ascii character")
x = input("Enter String ")
for i in x:
    print(i ,"=", ord(i))


print('''Search a word existence inside a given string
(Wikipedia is a free online encyclopedia, created and edited by volunteers around the world)''')
x = "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world"
y = input("Enter world to search ")
print("online" in x)


# Check the given 2 strings are anagrams.
print("Check the given 2 strings are anagram")
x = input("Enter two string ")
y = input("Enter other sting ")
set1 = set()
set2 = set()
for i in x:
    set1.add(i)
for i in y:
    set2.add(i)
print(set2 == set1)


# Take two strings from the input, join those two strings with a space and print the new string
print("Take two strings from the input, join those two strings with a space and print the new string")
x = input("Enter  string ")
y = input("Enter other sting ")
print(" ".join([x,y]))

# Take a string from the input and print the first character of that string
print("Take a string from the input and print the first character of that string")
x = input("Enter  string ")
print(x[0])


# Take a string from the input and print the first character and last characters of the string together
print("Take a string from the input and print the first character and last characters of the string together")
x = input("Enter  string ")
print(x[0] + x[-1])


# Take a string from the input and check all the letters in the string are of upper case
print("Take a string from the input and check all the letters in the string are of upper case")
x = input("Enter  string ")
print(x.isupper())


# Take two strings from the input and check the lengths of those strings equal or not
print("Take two strings from the input and check the lengths of those strings equal or not")
x = input("Enter 1st string ")
y = input("Enter other sting ")
print(len(x)==len(y))


# Take a string from the input and split the strings with comma. Print the new strings one per line
print("Take a string from the input and split the strings with comma. Print the new strings one per line")
x = input("Enter  string ").split(",")
for i in x:
    print(i)


# Take a string from the input and change lowercase characters to uppercase and uppercase characters to lowercase
print("Take a string from the input and change lowercase characters to uppercase and uppercase characters to lowercase")
x = input("Enter  string ")
list= []
temp = ""
for i in x:
    list.append(i)
for i in list:
    if i.isupper():
        temp = temp + i.lower()
    else:
        temp = temp + i.upper()
print(temp)
# Take a string from the input and remove all occurrences of given char from that string
print("Take a string from the input and remove all occurrences of given char from that string")
x = input("Enter  string ")
y = input("Enter character ")
new = ""
for i in x:
    if i == y:
        continue
    else:
        new = new + i
print(new)


# Count the total vowels and consonants in a given string and print them
print("Count the total vowels and consonants in a given string and print them")
x = input("Enter  string ")
cons = 0
Vol = 0
Vowels = "a e i o u A E I O U"
for i in x:
    if i in Vowels:
        Vol += 1
    else:
        cons =+ 1
print("Total Vowels    ", Vol,"\nTotal Consonant ", cons)


# Check whether or not the given string is a palindrome
print("Check whether or not the given string is a palindrome")
x = input("Enter  string ")
y = x[::-1]
print(x == y)

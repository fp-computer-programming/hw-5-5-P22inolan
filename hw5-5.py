# Author: IBN (AMDG) 10/29/2021

# Question 1
string = input("Give me a string. ")
half1 = string[:5]
half2 = string[5:]
print(half1)
print(half2)

# Question 2
letters = input("give me a six letter word. ")
odd = letters[0:1] + "/" + letters[2:3] + "/" + letters[4:5]
even = letters[1:2] + "/" + letters[3:4] + "/" + letters[5:6]
print(odd)
print(even)

# Question 3
palindrome = input("Give me a string. ")
reverse = palindrome[::-1]
if reverse == palindrome:
    print(reverse + " is a palindrome of " + palindrome)
else:
    print(reverse + " is not a palindrome of " + palindrome)

# Question 4
three = input("Give me three unique words. ")
words = [word.lower() for word in three.split()]
words.sort()
print("The alphabetized words:")
for word in words:
    print(word)
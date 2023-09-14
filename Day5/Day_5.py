# 1. Create a program that takes a user's name and age as input and prints a greeting message 

# name = input ("Enter your Name : ")
# age = int(input("Enter your age : "))
# print (f"HI {name}!, Your age is {age}. ")

#2. Write a program to check if a number is even or odd

# num = int(input ("Entter a number"))
# if num%2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

def even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number : "))
result = even_odd(num)
print(f"{num} is {result} number")

# Given a list of numbers, find the maximum and minimum values 

list_number = [10, 30,25,6, 78]

print(max(list_number))
print(min(list_number))

# Create a Python function to check if a given string is a palindrome 

import sys

def is_palindrom(word):
    word = word.replace("","")
    return word == word[::-1]

word = sys.argv[1]
if is_palindrom(word):
    print("f{word} is palindrom")
else:
    print(f"{word} is not palindrom")

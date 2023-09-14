# Write a program that add two numbers 

# pre-defined variable 
# a = 10
# b = 20

# Take varible from user input 

# a= float(input("Enter the number A : "))
# b= float(input("Enter the number B : "))

# sum = a+b
# print (sum)

import sys

def add_numbers(num1, num2):
    result = num1 + num2
    return result
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

sum = add_numbers(num1, num2)
print(sum)
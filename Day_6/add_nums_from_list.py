# Given a list of integers, find the sum of all numbers

# num = [2, -5, 20, 34, -21, 23]

# result = sum(num)
# print (result)

# using function

# def add_num (num):
#     result = sum(num)
#     return result
# num = [2, -5, 20, 34, -21, 23]
# sum_of_num = add_num(num)
# print (sum_of_num)

# Given a list of integers, find the sum of all positive numbers
# positive_num =0
# for num in num:
#     if num > 0:
#         positive_num +=num
# print(positive_num)
    
# using function 

def positive_num(num):

    positive_num =0
    for num in num:
        if num > 0:
            positive_num +=num
    return positive_num
num = [2, -5, 20, 34, -21, 23]
num = positive_num(num)
print(num)

# ( Create a program that takes a sentence as input and
# counts the number of words in it
#  ( Implement a program that swaps the values of two
# variables
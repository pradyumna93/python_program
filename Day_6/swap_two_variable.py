# Implement a program that swaps the values of two variables

# a = 10
# b = 20

# # swap two varivle
# temp = a
# a = b
# b = temp
# print(f"a = {a}")
# print(f"b = {b}")


# using function 

def swap_var(a,b):
    temp = a
    a = b
    b = temp
    return a, b

a,b = swap_var(10,20)
print(f"a = {a}")
print(f"b = {b}")
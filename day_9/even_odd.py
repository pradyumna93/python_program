
import sys

num = float(sys.argv[1])

# if num % 2 == 0:
#     print("Entered number is even")
# else:
#     print("Entered Number is Odd")

# using function

def odd_even (num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
result = odd_even(num)

print(f"Entered number is {result}")
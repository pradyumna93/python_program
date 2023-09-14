import sys

def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
    
num = int(sys.argv[1])
result = odd_even(num)
print(f"{num} is a {result} number")
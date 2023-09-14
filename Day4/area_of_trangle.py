

import sys

# Convert temperature from Celsius to Fahrenheit. 

# celsius = float(input("Enter the Celsius : "))
# Fahrenhit = (celsius*9/5)+32
# print(f"After converct the value of celsius is {Fahrenhit}F")

# def area_of_trangle(base, height):
#     result = 1/2*base*height
#     return result

# base = int(sys.argv[1])
# height = int(sys.argv[2])
# area = area_of_trangle(base, height)
# print(area)

def area_of_trangle(base, height):
    result = 1/2*base*height
    return result

base = float(sys.argv[1])
height = float(sys.argv[2])
print(area_of_trangle(base, height))
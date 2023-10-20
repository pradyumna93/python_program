
import sys

num1= int(sys.argv[1])
num2 =int(sys.argv[2])
num3 = int(sys.argv[3])

def largest_number(num1, num2, num3):
    if num1>num2 & num1 > num3:
        return "Num1 is grater"
    elif num2>num1 & num2>num3:
        return "num2 is grater"
    else:
        return "num3 is grater"
    
result = largest_number(num1, num2, num3)
print(result)
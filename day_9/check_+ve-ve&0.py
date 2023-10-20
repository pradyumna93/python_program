
# num = int(input("Enter the number : "))

# if num >0:
#     print("Number is +ve ")
# elif num == 0:
#     print("Number is queal to 0")
# else:
#     print("Number is -ve ")


# using function 

def check_number (num):
    if num >0:
        return "+ve"
    elif num < 0:
        return "-ve"
    else:
        return "0"
num = float(input("Enter the number :"))
result = check_number (num)
print(f"The input number is {result}")
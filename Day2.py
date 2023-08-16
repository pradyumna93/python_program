# Datatypes

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a twodigit number : ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result=int(first_digit)+int(second_digit)
print(result)


# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/be5ff193-a1ad-4f8e-ba40-504c85610518/BMI+Image+Small.jpeg

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_as_float = float(height)
weight_as_int = int(weight)
bmi = weight_as_int/height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Hint
# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x = 90 - int (age) 
y = 90 - int (age) 
z = 90 - int (age) 
days_remaining = x * 365 
week_remaining = y * 52
months_remaining = z * 12
print (f"You have {days_remaining} days, {week_remaining} weeks, and {months_remaining} months left.")

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_price = float(input("Enter the bill price: " ))
tips = int(input("Enter the tips price how much % you want to pay: "))
persons = int (input("Enter the person figure, with whom you want to split the bill: "))

result = (bill_price/(tips/100))/persons
final_amount = int(result)
print(f"Each person should pay {final_amount}")

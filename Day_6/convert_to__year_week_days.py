# Write a program that converts a given number of days into years, weeks, and days
def convert_number(total_days):
    years = total_days // 365
    remaing_days = total_days % 365
    weeks = remaing_days // 7
    days = remaing_days % 7
    return years , weeks, days

total_days = int(input("Enter the total days : "))

Years, Week, days = convert_number(total_days)
print(f"After convert the {total_days} we got aprox {Years}Years, {Week}week, {days}days")


# ( Given a list of integers, find the sum of all positive
# numbers
# ( Create a program that takes a sentence as input and
# counts the number of words in it
#  ( Implement a program that swaps the values of two
# variables
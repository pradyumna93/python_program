def check_leap_year(year):
    if year%400 == 0 and year%100 == 0:
        return "Leap year"
    elif year%100 !=0 and year%4 ==0:
        return "a Leap year"
    else:
        return "Not a Leap Year"
    
year = int(input("Enter the year to check Leap year or Not : "))

result = check_leap_year(year)
print (f"{year} is {result}")
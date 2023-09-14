# Calculate the compound interest for a given principal
# amount, interest rate, and time period

def compound_intrest(p , r, n, t ):
    final_amount = p*(1+r/n)**(n*t)
    return final_amount

p = float (input(" Enter the principal Amount : "))
r = float (input(" Enter the intrest rate : "))
n = float (input(" Enter the intrest applied per time peried : "))
t = float (input(" Enter how many times period elapsed : "))

finanal_amount = compound_intrest(p , r, n, t )

print(finanal_amount)

# P = principle_balance
# r = intrest_rate
# n = intrest_applied per time period
# t = period_elapsed


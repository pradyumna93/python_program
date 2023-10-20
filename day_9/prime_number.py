import sys

num = int(sys.argv[1])

def prime_number(num):
    if num ==1:
        return False
    if num >1:
        for i in range (2, num):
            if i % 2 == 0:
                return False
            else:
                return True
result = prime_number(num)
print(f"Entered number is a {result} number")
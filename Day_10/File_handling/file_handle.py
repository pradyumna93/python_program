"""file = open ('pradyumna.txt', 'r') # File is opened and ready for read
content = file.read () # Read the file and store in content
print(content)"""

# Use command line for run the program

"""file = open ('pradyumna.txt', 'r') # File is opened and ready for read
Line = file.readline()  # Read the first line of the conntent inside file
print(Line)"""

"""file = open ('pradyumna.txt', 'r')
lines = file.readlines() # It will the the whole line of the content one by one
print(lines)"""

"""file = open ('pradyumna.txt', 'w') # File is opened and ready to write
file.write('I am now working on Devops')

file = open ('pradyumna.txt', 'r')
content = file.read () 
print(content)"""

file = open('pradyumna.txt', 'a')
file.write("\nI am from India")
file = open ('pradyumna.txt', 'r')
content = file.read () 
print(content)
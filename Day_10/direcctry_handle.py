import os
import os.path
import shutil

os.mkdir('dir1') # Create a directry
a = os.listdir('.')
print (a)

x = os.path.exists ("D:/Python program/100_days_Python/Day_10/File_handling/pradyumna.txt")
y = os.path.exists ('dir1')

print('The existance of file is : ', x)
print('The existance of directry is : ', y)


os.rmdir('dir1') # remove the directry
os.remove('pradyumna.txt') # remove the file
shutil.rmtree('abc') # remove directy along with inside file or directry


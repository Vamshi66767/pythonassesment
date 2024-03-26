#1 read text file
from tabnanny import filename_only


file = open ('C:\\Users\\DELL\\OneDrive\\Desktop\\python\\vamshi.txt.txt', 'r')
print(file.read())

#-->2)

f = open('C:\\Users\\DELL\\OneDrive\\Desktop\\python\\vamshi.txt.txt','w')
f.writelines (input())
f.close()
#--->3)
try:
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\python\\vamshi.txt.txt','r') as file:
       for line in file:
           print(line, end = '')
except FileNotFoundError:
 print("file not found")
except IOError:
 print("an error occured while readind the flie")

#--4)
try:
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\python\\vamshi.txt.txt', 'rb') as file:
     file.seek(3)
     data = file.read(4)
     print(data.decodes('utf-8'))
           
except FileNotFoundError:
   print("file not found")
except IOError:
 print("an error occured while readind the flie")

 import os
def checking_permissions(filename):
   if os.access(filename, os.R_OK):
        print(f"file '{filename}' has read access.")
        print(filename)
   if os.access(filename, os.W_OK):
        print (f"File '{filename}' has write access.")
   else:
       print(f"file '{filename}' has does not have access.")     
filename = "C:\\Users\\DELL\\OneDrive\\Desktop\\python\\vamshi.txt.txt"  
checking_permissions (filename)

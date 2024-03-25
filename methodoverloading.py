#1) method overloading
def overload(a,b): 
 return a+b
print(overload(2,3))

def overload(a,b,c):
 return a+b+c 
print(overload (1, 2, 3))

#2) 

def overload(a,b): 
 return str(a) + ' age is '+str(b) 
print(overload('vamshi', 23))

def overload(a,b,c): 
 return str(a)+'scored'+str(b+c) 
print(overload('vamshi', 95, 1/2))

#3)
def overload(a,b): 
 return a+b 
 print(overload(2,3))

def overload(a,b):
 return a+b 
print(overload(1, 5))
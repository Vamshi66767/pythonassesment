# Write a function for arithmetic operators(+,-,*,/)

num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
  
sum = float(num1) + float(num2)  
min = float(num1) - float(num2)  
mul = float(num1) * float(num2)  
div = float(num1) / float(num2)  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  

# Write a method for increment and decrement operators(++, --)

a = 0
a += 1
a = a+1
print('The value of a is ',a)
print("INCREMENTED FOR LOOP")
for i in range(0, 5):
   print(i)
print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):
   print(i)

# Write a program to find the two numbers equal or not.

a=input('enter firts number')
b=input('enter second number')
if a==b:
   print("both numbers are equal")
else: 
   print("both numbers are not equal")

# Program for relational operators (<,<==, >, >==)

a=9
b=6
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)

 # print the smaller and larger number

a=float(input('enter first number:'))
b=float(input('enter second number:'))

a>b;
print(a,"is greater")
print(b,"is greater")

a<b;
print(a,"is smaller")
print(b,"is smaller")




# python
user input
username = input("Enter username:")
print("Username is: " + username)
# add the two numbers with user input
num1=input('enter the first number:')
num2=input('enter the second number:')
# Add two numbers
print(num1 + num2)
"""
"""
# user input
# Python program showing  
# a use of input()  
name = input("Enter your name: ")  # String Input  
age = int(input("Enter your age: ")) # Integer Input  
marks = float(input("Enter your marks: ")) # Float Input  
print("The name is:", name)  
print("The age is:", age)  
print("The marks is:", marks)  
"""
"""
#typecasting method
# add the two numbers with user input
num1=input('enter the first number:')
num2=input('enter the second number:')
# Add two numbers
sum=float(num1)+float(num2)
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
# Python automatically converts variable into desired data type
a = 7
print(type(a))
b = 3.0
print(type(b))
c = a + b
print(c)
print(type(c))
d = a * b
print(d)
print(type(d))
"""
"""
a=input("enter the value of a:")
print("value of a is:",a)
print(type(a))
b=input()
print(b)
print(type(b))
"""
"""
a=int(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=int(input("enter the value of c:"))
d=str(input("enter the value of d:"))
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(bin(45))
print(bin(20))
print(float(0b10010))
print(int(0b100))
print(a+b)
print(a+c)
print(c+d)
"""
"""
# tuple Example
a=(2,5.4,True,3+5j,[1,2,3])
print(a[::4])
print(a)
print(type(a))
b=(2,8.9,"qwerty",4+9j,True,[11,44,66])
print(b)
print(type(b))
print(b[-3])
print(b[2])
print(b[2][-1::-5])
print(b[-1:0:-2])
"""
"""
#count function
a=(28.9,7.4,2,3,2,2,4,2,3,18,1,1,1,4+6j,True,[23,56,10])
print(a)
print(type(a))
print(a.count(2))
print(a.count(3))
print(a[-1].count(56))
print(a.count(1))
"""
"""
a=(28.9,7.4,2,3,2,"qwerty",2,4,2,3,18,1,1,1,4+6j,True,[23,56,10])
print(a.index("qwerty"))
print(a.index(2))
#print(a.index(::-6))
print(a[-1].index(10))
print(a.index(28.9))
#a[0]=78
#print(a)
a[-1].append(44)
print(a)
#del a[1]
del a
print(a)
      
"""
a,b=(1,2),(3,4)
print(a)
print(b)
print(a+b)
print(a*3)
c=(45)
print(c,type(c))
d=("hii")
print(d,type(d))
e=(2,)
print(e,type(e))


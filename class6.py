"""
# if else condition
a=6
if a>7:
    print("Hello")
else:
    print("done")

#pass keyward
print("start")
if True:
    pass
print("done")
"""
"""
# without logical operator
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=  int(input("enter the value of c:"))
if a>b:
    print("start")
    if a>c:
        print("a is greatest")
           
elif b>c:
     if b>a:
         print("b is greatest")
        
else:
    print("c is greatest")
"""


"""
#nested if
x=19
if x>10:
    print("x is greater thna 10")
    if x>2:
        print("x is greater than 20")
    elif x>10:
        print("hello")
    else:
        print("but not 20")
elif x>2:
    print("hii")
else:
    print("done")
"""
"""
#without logical operator
a,b,c=14,25,6
if a>b:
    if a>c:
        print("a is greatest")
elif b>c:
    if b>a:
        print("b is greatest")
else:
    print("c is greatest")
"""
"""
a,b,c=12,4,48
if a>b and a>c:
    print("both conditions are true")
    if a>b or a>c:
           print("anyone condtidions is true")
else:
    ("only c true")
"""
#loops
#while loop
"""
#increment operator
a=1
while a<=5:
    
    print("hello",a)
    a+=1
print("exit")
"""
"""
#decrement operator
a=11
while a>2:
    
    print("hello",a)
    a-=1
print("exit")
"""
"""
#first first 10 numbers
a=1
while a<=10:
    print(a)
    a+=1
print("done")
"""
"""
# table of 5
a=1
while a<=10:
    print(5*a)
    a+=1
print("done")
"""
"""
#table generator
b=(int(input("enter the velue of b:")))
a=1
while a<=10:
    print(b*a)
    a+=1
print("done")
"""
"""
b=(int(input("enter the velue of b:")))
a=1
while a<=10:
    print(b,"x",a,"=",b*a)
    a+=1
print("done")
"""
# star printing
"""
a=1
while a<=5:
    print("*",end="")
    a+=1
"""
"""
b=1
while b<=4:
    a=1
    while a<=5:
        print("*",end="")
        a+=1
    print()
    b+=1
"""
"""
b=1
while b<=5:
    a=1
    while b>=a:
        print("*",end="")
        a+=1
    print()
    b+=1
"""

b=1
while b<5:
    a=4
    while b<=a:
        print("*",end="")
        a-=1
    print()
    b+=1


    
    
    
        
        
    

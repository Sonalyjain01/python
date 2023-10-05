"""
#-------------------------
#Task 4
def add(*b):
    a=0
    for i in b:
        a=a+i
        print(a)           
add(2,3,5,67,8, 12,32,20)

"""
"""
#-----------------------------
#task 3
def add(*b:int(input("enter the number"))):
    a=[]
    c=[]
    for i in b:
        a.append(i*12)
        print("Mul of a:",a)
    for j in b:
        c.append(i+12)
        print("Sum of a:",c)
        
add(2,3,5,67,8, 12,32,20)
"""
"""
#---------------------------
#task 1
#def sum(a:int(input("enter the value of a:")),*b:int(input("enter the value of  b :"))):
def sum(a,*b):
    x=0
    for i in b:
        x=x+i 
        print(x+a)
    print("value of a is:",a)
    print("value of b is:",b)
    print(type(a))
    print(type(b))
    print(type(x))
sum(2,12,45,60,30,6,8,34)
"""

#---------------------------
#task 2
#def even_odd(*a: int(input("enter the value of a:"))):
def even_odd(*a):
    x=[]
    y=[]
    for i in a:
        if(i%2==0):
            x.append(i)
        else:
            y.append(i)
    print("Even numbers :",x)
    print("Odd numbers :",y)
    print(type(x))
    print(type(y))
even_odd(12,57,77,11,34,36,8,6,2,51)



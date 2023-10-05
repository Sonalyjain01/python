#-------------------------------
"""
# Abstraction
a,b=3,8

print("addition:",(a+b))
print(int.__add__(a,b))
#print(int.__add__(a,b,c))
print("Subtraction:",(a-b))
print(int.__sub__(a,b))
print("multiplication:",(a*b))
print(int.__mul__(a,b))
print("division:",(a/b))
print(int.__truediv__(a,b))
"""
#-----------------------------------
"""
class college:
    name="xyz"
    country="India"
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        print(m1+m2)
        print(int.__add__(m1,m2))
        print("done")
    def __add__(x1,x2):
        print("addition")
    def __sub__(x1,x2):
        print("Subtraction")
s1=college(34,21)
s2=college(27,26)
s1+s2
s1-s2
"""
#-----------------------------------
"""
class college:
    name="xyz"
    country="India"
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(x1,x2):
        #rowwise addition
        a=x1.m1+x1.m2
        b=x2.m1+x2.m2
        print("addition:",(a,b))
        #column wise addtion
        a=x1.m1+x2.m1
        b=x1.m2+x2.m2
        print("addition:",(a,b))
        
    def __sub__(x1,x2):
        #row wise substraction
        a=x1.m1-x1.m2
        b=x2.m1-x2.m2
        print("substraction:",(a,b))
        #column wise subtraction                       
        a=x1.m1-x2.m1
        b=x1.m2-x2.m2
        print("substraction:",(a,b))
    def __mul__(x1,x2):
        #row wise multiplication
        a=x1.m1*x1.m2
        b=x2.m1*x2.m2
        print("multiplication:",(a,b))
        #column wise multiplication                  
        a=x1.m1*x2.m1
        b=x1.m2*x2.m2
        print("multiplication:",(a,b))
    def __truediv__(x1,x2):
        #row wise division
        a=x1.m1/x1.m2
        b=x2.m1/x2.m2
        print("division:",(a,b))
        #column wise division                    
        a=x1.m1/x2.m1
        b=x1.m2/x2.m2
        print("division:",(a,b))
s1=college(34,21)
s2=college(27,26)
s1+s2
s1-s2
s1*s2
s1/s2
"""
#-------------------------------
# polymorphism
"""
# Method overloading
class Abc:
    def add(a,b):
        print(a+b)
    def add(a,b,c):
        print(a+b+c)
    def add(a,b,c,d):
        print(a+b+c+d)
a=Abc()
a.add(2,6,7)
"""



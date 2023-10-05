"""
def add(a,*b):
    print( a)
    print(b)

add(2,7,67,18)

#-------------------------
#arbitary arguments
def add(*b):
    a=0
    for i in b:
        a=a+i
        print(a)           
add(2,3,5,67,8)
"""

#----------------------------
def welcome(*a):
    
    for i in a:
        
        print("welcome:",i)
welcome(1,"abc",2,14,54,7,8,18,True,4+
        6j)
"""    
#-------------------------------
#anonymous function
b=lambda a: print( "Square is:",a*a) 
b(5)
x=lambda d,c,:print("Sum of c & d is:",c+d)
x(23,6)

#-----------------------------------
x=lambda a,*b:print("value of a & b is:", a, b) 
x(12,23,5,8,3,56)
"""

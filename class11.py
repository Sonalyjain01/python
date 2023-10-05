"""
#---------------------
# filter function
a=[2,4,6,8,1,3,5,7,9]
print(a)

x=list(filter(lambda x:x%3==0,a))
print(x)

def even(n):
    if n%2==0:
        return a
#x=list(filter(even,a))
print(x)
"""
"""
#----------------------
#map function
a=[2,4,6,8,1,3,5,7,9]
print(a)
def even(n):
    return n*5    
x=list(map(even,a))
#x=list(map(lambda  x:x*2,a))
#x=list(map(lambda x:x%2==0,a))
print(x)

"""
"""
#---------------------------
#reduce function
from functools import reduce
a=[2,4,6,8,1,3,5,7,9]
print(a)
w=reduce(lambda a1,b1:a1+b1,a)
print(w)

def add(a1,b1):
    return a1+b1
w= reduce(add,a)
print(w)
"""
"""
#-----------------------------
#local variables & global variable
a=6 # global variable
def f1(a):
    a=4 # local variable
    print(a)
f1(a)
print(a)
"""
#---------------------------------
# global keyword
"""
x=15
def f1():
	# using a global keyword
	global x
	x = x + 5
	print("Value of x  :", x)
f1()
print("Outside value of x :", x)
"""
#--------------------------------
"""
#global function
a = 2
b = 5
c = 9
def f1():
    a=8
    print("local var:",a)
    x=globals().get("b")
    print(x)
    y=globals().get("a")
    print(y)
    z=globals().get("c")
    print(z)
f1()
"""

# global variable
a = 5

def f1():
	c = 10
	d = c + a
	# globals()
	globals()['a'] = d
	print (a)
f1()


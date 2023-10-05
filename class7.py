#membership operator
"""
a={4,7,1,"abc",74}
print(a)
print(4 in a)
print("abc" in a)
print(4 not in a)
print(44 not in a)

#identity operator
a,b,c=2,4,2
print(a is c)
print(a is b)
print(a is id(c))
print(b is id(a))
print( b is not c)
print(c,id(c))
print(b,id(b))
print(a,id(a))
"""
"""
#for loop
#define squence
#for i in (45,12,34,90):
    #print(i)
#for i in [34,34,12,'abc',90]:
    #print(id(i))
for i in {3,4,1,8,9,'abc',4,1,2,3,4}:
    print("xyz")
print("end")

a={
    'name':'abc',
    'age': 23
    }
#for i in a:
    #print(i)
#for i in a.values():
    #print(i)
#for i in a.items():
    #print(i)

#for i,j in a.items():
    #print(i,j)
for i in "qwerty":
    print('x')
    print("done")
"""
#range
"""
print(range(2,7,1))
for i in range(2,7,1):
    print(i)
print("-----------------------")
for i in range (2,6,1):
    print(i)
print("-----------------------")
for i in range (6,16,2):
    print(i)
print("-----------------------")
for i in range(5):
    print(i)
print("-----------------------")
for i in range(5,10):
    print(i)
print("-----------------------")
for i in range(10,5):
    print(i)
print("-----------------------")
for i in range(10,4,-1):
    print(i)
"""

#for i in range():
"""
a=int(input("enter the vlaue of a:"))
for i in range(1,11,1):
    print(i*a)
 """
"""
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
if a>b:
    for i in range (a,b-1,-1):
        print(i)
elif b>a:
    for i in range (a,b+1,1):
        print(i)
    
else:
    print("values are same")
"""
"""
#pattern

for i in range(1):
    print("*")
#----------------------------------
print("-------------------------------")

for i in range(1,6):
    print("*")

#----------------------------------
print("-------------------------------")

for j in range(4):
    for i in range(5):
        print("*",end="")
    print()


for i in range(0,5):
    for j in range(i+1):
        print("*",end="")
    print()


for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()


a=input("enter the value of a:")
for i in range(len(a)):
    for j in range(i+1):
        print(a[j],end="")
    print()
"""
a=input("enter the value of a:")
for i in range(len(a)):
    for j in range(i+1):
        print(a[i],end="")
    print()


    
      
    

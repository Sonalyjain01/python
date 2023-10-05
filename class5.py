"""
student={
    "name":"abc",
    "age":31,
    "skills":["python","ml"]
    }
#fromkeys function
print(student.fromkeys(["name","age","skills"],124))

a=student.fromkeys(["name","age","skills"],"sunoo")
print(a)

"""
"""
#setdefault function
print(student)
print(student.setdefault("rollno",112))
print(student)
student.setdefault("name1","qwerty")
print(student)
"""
"""
#set data type
a={2,7,2,2,2,True,11,1}
print(a)
print(type(a))
b={23,5.7,"ahc",(33,56,32),True,4+6j}
print(b)
print(type(b))
# add the value
a={2,7,2,2,2,True,11,1}
print(a)
a.add(23)
print(a)
a.add((145,78,"abc"))
print(a)
"""
"""
#update function
a={2,7,2,2,2,True,11,1}
print(a)
a.update((33,56,"qwerty",7+5j))
print(a)
a.update({40,96,"carry",2+5j})
print(a)
"""

#remove method
"""
#clear function
a={2,7,2,2,2,True,11,1}
print(a)
a.clear()
print(a)
a.add((23,67,45,21))
print(a)
print("done")
#print(a)
"""
#del function
"""
#pop function
a={2,7,2,2,2,True,11,1}
print(a)
a.add((23,67,45,21))
print(a)
#del a
a.pop()
print(a)
print("done")

#remove function
a={2,7,2,2,2,23,True,11,1}
print(a)
a.add((23,67,45,21))
print(a)
a.remove(23)
print(a)
print("done")
a.remove(12)
print(a)
#discard function
a={2,7,2,2,2,23,True,11,1}
print(a)
a.add((23,67,45,21))
print(a)
a.discard("abc")
print(a)
a.discard(7)
print(a)
print("done")
"""

# operations of set
"""

a,b={1,2,3,4},{3,4,5,6}
print(a)
print(b)
print(a.symmetric_difference(b))
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
result=A.symmetric_difference_update(B)
print(result)

a,b={1,2,3,4},{3,4,5,6}
print(a)
print(b)
a.symmetric_difference_update(b)
print(a)
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e','f'}
A.symmetric_difference_update(B)
print(A)

#print(a-b)
#print(b-a)




#print(a.intersection(b))
#print(a.union(b))
#print(a/b)
#print(a+b)

"""
"""
#control statement

# if statement
a=int(input("enter the value of a:"))
if a>10:
    print("inside if")
    print("start")
    print(a)
    print("end")
print("outside if")
"""
"""
#if else statement
a=int(input("enter the value of a:"))
if a>10:
    print("inside if")
    print("start")
    print(a)
    print("end")

else:
    print("value of a is less than 10")
print("outside if")
"""

# if-elif-else statement
a=int(input("enter the value of a:"))
if a>10:
    print("a is greater than 10")
elif a==10:
    print("a is equals to 10")
else:
    print("a is less than 10")
print("done")

    


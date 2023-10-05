"""
a=[3,1,'abc', True,[22,44,55,77,88]]
print(type('abc'))
print((a[4][-1:-6:-4]))
print(type(a[4][-1:-6:-4]))
print(a[0:6:4])
"""
"""
a=[3,1,'abc', True,[22,44,55,77,88]]
print("before:",a)
a[4][2]=True
print("after:",a)
a[2]=100
print("after:",a)
"""
"""
#It show the some error
a[1:2]=100
print("after:",a)
"""
"""
#append function.
a=[3,1,'abc',True,]
print(a)
a.append(100)
print(a)
a.append([22,45,66,'sona'])
print(a[-2])
a[-1].append(400)
print(a)
"""
"""
#insert function.
a=[3,1,'abc',True,[10,200]]
a.insert(3,300)
print(a)
a[-1].insert(2,100)
print(a)
a.insert(-1,600)
print(a)
"""
"""
#extend function.
a=[3,1,'abc',True,[10,200]]
a.extend([22,33,44])
print(a)
a.extend("abc")
print(a)
a.extend(["abc"])
print(a)
a.extend([[2,4,5],[3,6,9]])
print(a)
a[-1].extend(["aaa","bbb"])
print(a)
"""
"""
#Remove the element.
a=[2,4,3,7,7,True,7,"abc",1,2,3,2,8,7,8,[44,55,66]]
print(a)
a.remove("abc")
print(a)
a.remove(True)
print(a)
a[-1].remove(55)
print(a)
"""
"""
#pop function.
a=[2,4,3,7,7,True,7,"abc",1,2,3,2,8,7,8,[44,55,66]]
a.pop(9)
print(a)
a.pop()
print(a)
"""
"""
a=[2,4,3,7,7,True,7,"abc",1,2,3,2,8,7,8,[44,55,66]]
#a.clear()
#print(a)
a[-1].clear()
print(a)
a.append(500)
print(a)
"""

#del function.
a=[2,4,3,7,7,True,7,"abc",1,2,3,2,8,7,8,[44,55,66]]
del a
print(a)
#del a[:7:2]
#print(a)
#del a[-1][::3]
#print(a)



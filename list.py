a=[2,8,1,'abc',[100,200]]
#print(a)
"""
a[2].extend([44,55,66])
print(a)
"""
#a[-1].insert(2,4)
#print(a)
#del a[-1][0:1]
#print(a[-1][-1:-3:-1])
"""
# index function
a=[2,8,1,'abc',[100,200]]
print(a)
#print(a.index('abc'))
b=[2,5,1,89,[33,44,55]]
#print(b[-1].index(44))
print(b[-1].index(33))
print(b.index(33))
"""
"""
# sort function
a=[2,5,1,89,33,44,55]
a.sort()
print(a)
a.sort(reverse=False)
print(a)
a.sort(reverse=True)
print(a)
b=['abc','bcd','lpg','eyz']
b.sort(reverse=False)
print(b)
c=[2,4,[55,96,77],34]
c[-2].sort()
print(c)
d=[23,45,'hii',True,2,0,1]
print(d)
d.sort()
print(d)
"""
"""
#count function
#d=[1,2,3,4,1,1,3,3,'bcd']
#print(d.count(1))
#print(d.count(3))
#print(d.count(4))
#print(d.count('abc'))
a=[2,8,1,'abc',[100,200,100,200,300,200,400]]
print(a[-1].count(100))
print(a[-1].count(200))
print(a.count(300))
print(a[-2].count(400))
"""
"""
# copy function
#a,b,c=1,2,1
#print(a,id(a),sep='\t')
#print(b,id(b),sep='\t')
#print(c,id(c),sep='\t')
a=[11.22]
b=[33,44]
c=a.copy()
print(a,id(a),sep='\t')
print(b,id(b),sep='\t')
print(c,id(c),sep='\t')
"""

# reverse function
a=[2,6,1,39,84,'abc',1,1,1,3,2,3,2,3,2,31,4]
print("before:",a)
a.reverse()
print("after:",a)
b=[2,6,1,39,84,'abc',[1,1,1,3,2,3,2,3,2,31,4]]
print("before:",b)
b[-1].reverse()
print("after:",b)


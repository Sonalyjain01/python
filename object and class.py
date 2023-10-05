"""
#------------------------------
class Abc:
    name="qwerty"
    age=12
a=Abc()
print(type(a))
"""
"""
#----------------------------
class A:
    name="a1"
    def __init__(x):
        print("init A")
class B:
    name="b1"
    def __init__(x):
        print("init B")
class C:
    name="c1"
    def __init__(x):
        print("init C")
a=A()
b=B()
c=C()
"""
"""
#-------------------------------
class A:
    name="abc"
    def __init__(self):
        print("init A")
a=A()
b=A()
c=A()
"""
"""
#-------------------------------
class College:
    name="Tmu"
    state="UP"
s1=College()
s2=College()
#s2.name="qwerty"
print(s1.name ,s1.state)
print(s2.name, s2.state)
"""
"""
#---------------------------------
class College:
    name="BIT"
    state="UP"
    def __init__(self,name,age):
        print("init college")
        #print(name,age)
s1=College()
#s1=College("aaa",21)
"""
#--------------------------------
class College:
    name="BIT"
    state="UP"
    def __init__(self,m1,m2):
        print(m1,m2)
        #self.m11=m1
        #self.m22=m2
        print("xyz")
    #def info(self):
        #print(self.m11,self.m22)
#s1=College(21,33)
s2=College(23,24)
#s1.info()
#s2.info()

#----------------------------------

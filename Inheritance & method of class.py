"""
#------------------------------------------
# class & instance method
class company:
    name="Eisystems"
    country="India"
    def __init__(self,name,eid):
        self.name1=name
        self.eid1=eid
    def info(self):
        print("name of the employee is {} and eid of the employee is {}".format(self.name1,self.eid1))
    @classmethod
    def info_cls(cls):
        print(cls.name,cls.country)
e1=company("sonaly",127)
e2=company("om",122)
#e1.info()
#e2.info()
#print(company.name)
#print(e1.name)
company.info_cls()
e1.info_cls()
"""

"""
#--------------------------------------
# static method
class company:
    name="Eisystems"
    country="India"
    def __init__(self,name,eid):
        self.name1=name
        self.eid1=eid
    def info(self):
        print("name of the employee is {} and eid of the employee is {}".format(self.name1,self.eid1))
    @classmethod
    def info_cls(cls):
        print(cls.name,cls.country)
    @staticmethod
    def add(a,b):
        print(a+b)
        
e1=company("sonaly",127)
e2=company("om",122)
e1.add(4,5)
company.add(3,8)
"""
#-------------------------------------
# Inheritance
"""

class A:
    def f1(self):
        print("f1 A")
    def f2(self):
        print("f2 A")
class B(A):
    def f3(self):
        print("f3 B")
a=A()
b=B()


a.f1()
a.f2()
b.f3()
b.f1()
b.f2()
"""
# Type of inheritance
"""
# multilevel
class A:
    def f1(self):
        print("f1 A")
    def f2(self):
        print("f2 A")
class B(A):
    def f3(self):
        print("f3 B")
class C(B):
    def f4(self):
        print("f4 C")
a=A()
b=B()
c=C()
a.f1()
a.f2()
b.f1()
b.f2()
b.f3()
c.f4()
c.f3()
"""
"""
# hyrerical
class A:
    def f1(self):
        print("f1 A")
    def f2(self):
        print("f2 A")
class B(A):
    def f3(self):
        print("f3 B")
class C(A):
    def f4(self):
        print("f4 C")
a=A()
b=B()
c=C()
a.f1()
b.f1()
c.f1()
c.f2()
b.f2()
b.f3()
c.f4()
"""
"""
# multiple
class A:
    def f1(self):
        print("f1 A")
    def f2(self):
        print("f2 A")
class B():
    def f3(self):
        print("f3 B")
class C(A,B):
    def f4(self):
        print("f4 C")
a=A()
b=B()
c=C()
#a.f1()
#b.f3()
c.f3()
c.f1()
c.f2()
c.f4()
"""

"""
# hybrid
class A:
    def f1(self):
        print("f1 A")
    def f2(self):
        print("f2 A")
class B():
    def f3(self):
        print("f3 B")
class C(A,B):
    def f4(self):
        print("f4 C")
class D(C):
    def f5(self):
        print("f5 D")
class E(C):
    def f6(self):
        print("f6 E")
    
a=A()
b=B()
c=C()
d=D()
e=E()
#a.f1()
#b.f3()
c.f3()
c.f1()
c.f2()
d.f1()
d.f2()
e.f3()
e.f1()
d.f4()
e.f4()
d.f5()
e.f6()
e.f2()
d.f3()
"""
#----------------------------------

# constructor in Inheritance
class A:
    def __init__(self):
        print("init A")
    def f1(self):
        print("f1 A")
class B(A):
    def __init__(self):
        print("init B")
        super().__init__()
    def f1(self):
        print("f2 B")

a=A()
b=B()
b.f1()

#---------------------------------
"""
# MRO
class A:
    def __init__(self):
        print("init A")
    def f1(self):
        print("f1 A")
class B:
    def __init__(self):
        print("init B")
        
    def f1(self):
        print("f2 B")
class C(A,B):
    def __init__(self):
        print("init C")
        super().__init__()
    def f1(self):
        print("f1 C")

a=A()
b=B()
#b.f1()
c=C()
"""

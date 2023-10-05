"""
#-----------------------------------------------
# Exception
a=int(input("enter the value of a:"))
b=int(input("ener the vale of b:"))
print("start")
print(a/b)

#----------------------------------------------
#logical error
a="12"
b="4
print(a+b)

#-----------------------------------------------
#run time error
a="12"
b="4"
print(a*b)

#----------------------------------------------
#compile time error
a=10
if a==10
print(True)
else
print(False)
"""
"""
#----------------------------------------------
# raise Exception
x=int(input("enter the value of x:"))
if (x<10):
    raise Exception("My Error")
else:
    print(x)
#----------------------------------------------
       
try: 
    x=int(input("enter the value of x:"))
    if (x<10):
        raise Exception("My Error")
    else:
        print(x)
except Exception:
     print("invalid value")

"""
"""
#---------------------------------------------------
# excetion handling(try, except,& finally blocks)
a=int(input("enter the value of a:"))
b=int(input("ener the vale of b:"))
x=[11,67,34,58]
print("start")
try:
    #print(x[10])
    print(x[2])
    print(a/b)
    eid=int(input("enter your employee id:"))
    print("your eid is:",eid)
except ZeroDivisionError:
    print("can't divide a number by zero")
except IndexError:
    print("Index out of range")
#except Exception:
    #print("something went wrong")
finally:
    print("done")
"""    
    
    

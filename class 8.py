#patterns
"""
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(end=" ")
    print()

#-------------
for i in range(7):
    for j in range(5):
        if i==3 or j==0 or j==4:
            print("*",end="")
        else:
            print(end=" ")
    print()


#--------
for i in range(7):
    for j in range(5):
        if i==0 or i==3  or j==0:
            print("*",end="")
        else:
            print(end=" ")
    print()


#------------
for i in range(7):
    for j in range(5):
        if i==0 or i==3 or j==0 or ((i==1 or i==2) and j==4):
            print("*",end="")
        else:
            print(end=" ")
    print()


#----------
for i in range(7):
    for j in range(5):
        if (((i==0 or i==3)and j<4) or (j==0 or (j==4 and i<3 and i>0))): 
        #if ((i==0 or i==3)and j>4) or (j==0 or((i==2 or i==1)and j==4))):
            print("*",end="")
        else:
            print(end=" ")
    print()


#--------------------
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or i==3 or (i==0 and j!=0 and j!=4):
            print("*",end="")
        else:
            print(end=" ")
    print()
"""

#----------------------------
for i in range(7):
    for j in range(5):
        if (i==0 and j!=0) or ((i==6 or i==3) and j!=4 ) or (j==0 and (i==1 or i==2 or i==6)) or (j==4 and (i==4 or i==5)) :
            print("*",end="")
        else:
            print(end=" ")
    print()


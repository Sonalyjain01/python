#---------------------------------
"""
# rectangular "O"
for i in range(6):
    for j in range(5):
        if i==0 or i==5 or j==0 or j==4:
            print("*",end="")
        else:
            print(end=" ")
    print()

#-------------------------------------
# print "H"
for i in range(7):
    for j in range(6):
        if  i==3 or j==0 or j==5:
            print("*",end="")
        else:
            print(end=" ")
    print()

#---------------------------------------
# print "F"
for i in range(7):
    for j in range(6):
        if  i==0 or i==2 or j==0:
            print("*",end="")
        else:
            print(end=" ")
    print()

#------------------------------------------
# circular "O"
for i in range(6):
    for j in range(5):
        if (i==0 and (j==1 or j==2 or j==3)) or (i==5 and (j==1 or j==2 or j==3 )) or (j==0 and (i==1 or i==2 or i==3 or i==4)) or (j==4 and (i==1 or i==2 or i==3 or i==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#-------------------------------------
# print  rectangular "P"
for i in range(7):
    for j in range(5):
        if  i==0 or i==3 or j==0 or (j==4 and (i==0 or i==1 or i==2 or i==3)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#----------------------------------------
# print circular "P"
for i in range(7):
    for j in range(5):
        if  ((i==0 or i==3) and j!=4) or j==0 or (j==4 and (i==1 or i==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------
# print rectangular "A"
for i in range(7):
    for j in range(5):
        if  i==0 or i==3 or j==0 or j==4:
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------
# print circular "A"
for i in range(7):
    for j in range(5):
        if  (i==0 and (j==1 or j==2 or j==3)) or i==3 or ((j==0 or j==4) and i!=0):
            print("*",end="")
        else:
            print(end=" ")
    print()

#----------------------------------------------
# print rectangular "S"
for i in range(5):
    for j in range(5):
        if  i==0 or i==2 or i==4 or (j==0 and i==1) or (j==4 and i==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

#------------------------------------------------
# print circular "S"
for i in range(7):
    for j in range(4):
        if  (i==0 and j!=0) or ((i==6 or i==3) and j!=3) or (j==0 and (i==1 or i==2))or(j==3 and(i==4 or i==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "E"
for i in range(7):
    for j in range(5):
        if  i==0 or i==3 or j==0 or i==6:
            print("*",end="")
        else:
            print(end=" ")
    print()

#-------------------------------------------------
#print "B"
for i in range(7):
    for j in range(5):
        if  (i==0 and j!=4) or (i==3 and j!=4)or j==0 or (i==6 and j!=4) or (j==4 and (i==1 or i==2 or i==4 or i==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------
# print rectangular "C"
for i in range(6):
    for j in range(4):
        if  (i==0 and j!=0) or (i==5 and j!=0) or (j==0 and (i==1 or i==2 or i==3 or i==4))  :
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "D"
for i in range(7):
    for j in range(5):
        if  (i==0 and j!=4) or (j==4 and (i==1 or i==2 or i==3 or i==4 or i==5)) or j==0 or (i==6 and j!=4):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
# print rectangular "G"
for i in range(6):
    for j in range(6):
        if  (i==0 and j!=0) or (i==5 and j!=0) or (j==0 and (i==1 or i==2 or i==3 or i==4)) or (j==3 and i==3) or (j==5 and (i==3 or i==4)):
                                                                                                        
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "I"
for i in range(7):
    for j in range(5):
        if  i==0 or j==2 or i==6:
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "T"
for i in range(7):
    for j in range(5):
        if  i==0 or j==2:
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "J"
for i in range(7):
    for j in range(7):
        if  i==0 or (j==3 and i!=6) or (i==6 and (j==1 or j==2)) or (i==5 and j==0):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "K"
for i in range(7):
    for j in range(5):
        if  j==0 or ((i==0 or i==6)and j==4) or (i==3 and j==1) or (j==2 and(i==4 or i==2)) or (j==3 and (i==1 or i==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "L"
for i in range(7):
    for j in range(5):
        if  i==6 or j==0:
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "M"
for i in range(7):
    for j in range(7):
        if  j==6 or j==0 or (i==1 and (j==1 or j==5)) or (i==2 and (j==2 or j==4)) or (i==3 and j==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

#--------------------------------------------------
#print "N"
for i in range(7):
    for j in range(7):
        if  j==6 or j==0 or (i==1 and j==1) or (i==2 and j==2) or (i==3 and j==3) or (i==4 and j==4) or (i==5 and j==5):
            print("*",end="")
        else:
            print(end=" ")
    print()
"""
#----------------------------------------------------
# circular "Q"
for i in range(6):
    for j in range(5):
        if (i==0 and (j==1 or j==2 or j==3)) or (i==5 and (j==1 or j==2 or j==3 )) or (j==0 and (i==1 or i==2 or i==3 or i==4)) or (j==4 and (i==1 or i==2 or i==3 or i==4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

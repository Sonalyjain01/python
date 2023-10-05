"""
#--------------------------
#task 1
#by using for loop
for i in range(4):
    for j in range(5):
        if i==0 or j==1  or j==0 or (j==2 and (i==1 or i==2)) or (j==3 and i==1):
            print("&",end="")
        else:
            print(end=" ")
    print()

#by using while loop
b=1
while b<5:
    a=5
    while b<=a:
        print("&",end="")
        a-=1
    print()
    b+=1
"""
"""
#----------------------------
#task 3
def num(*a):  
    for i in a:
        if(i%5==0):
            print("divisible by 5 :",i)
num(15,10,56,9,40,3,6,75,8,30)

#--------------------------------
#task 2
a=("My Name Is Python")
print(a[0:17:2])
"""

#---------------------------------
#task 6
a=[2,3,4,5,6,7,8,9,10,11,12]
print("Original list:",a)
square=list(map(lambda x:x*x,a))
print("square:",square)
cube=list(map(lambda y:y**3,a))
print("cube:",cube)
"""
#---------------------------------
#task 4
def is_palindrome(a):
    a=a.replace(" ","").lower()
    b=a[::-1]
    if a==b:
        return "string is palindrome"
    else:
        return "String is not palindrome"
x=input("Enter a string: ")
result=is_palindrome(x)
print(result)
"""
#------------------------------------
"""
#task 5
def remo_wood(a):
    if (a%3==0):
        return "remo"
    elif (a%3 and 5==0):
        return "remo_wood"
    elif (a%5==0):
        return "wood"
    else:
        return a
b=int(input("Enter a number:"))
x=remo_wood(b)
print(x)
"""   

    


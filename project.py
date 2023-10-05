def add():
    eid=input("enter the employee id: ")
    name=input("enter name of the employee: ")
    cn=input("enter the phone number of employee: ")
    state=input("enter state of the employee: ")
    #creating file using file handling
    f=open("employeeinfo.txt","a")
    f.write(eid+"\t")
    f.write(name+"\t")
    f.write(cn+"\t")
    f.write(state+"\n")
    print("record added")
    f.close()
def show():
    f=open("employeeinfo.txt","r")
    print("Eid\t Name \t Phone no. \t state \n")
    print(f.read())
    print("record show")
def delete():
    i=input("enter the eid of the employee")
    with open("employeeinfo.txt","r") as f:
        a=f.readlines()
    with open("employeeinfo.txt","w") as f:
        for b in a:
            b1=b.split("\t",1)
            if (b1[0]!=i):
                f.writelines(b)
        print("record deleted")
        
while True:
    print("---------------Welcome to data feeding application--------------------")
    print("1. Add new employee record")
    print("2. delete employee record")
    print("3. show employee record")
    print("4. exit")
    n=int(input("enter your choice :"))
    if n==1:
        add()
    elif n==2:
        delete()
    elif n==3:
        show()
    else:
        exit()
   


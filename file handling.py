"""
#-------------------------
#create and write the file
open("abc.txt","w")
a=open("abc.txt","w")
a.write("I am myfile")
a.close()

"""
#-------------------------
#read the file
a=open("abc.txt","r")
print(a.read())
"""
#-----------------------
#append the file
a=open("abc.txt","a")
a.write("python")
a.close()
"""
#-----------------------
#create a py file
#edit in the file
open("aaa.py","w")
#------------------------

#create the pdf and mp4 file
#open("qwerty.pdf","w")
#open("qwerty.mp4","w")


#---------------------------
#import zipfile
#x=zipfile.ZipFile("myzipfile.zip","w")
#x.write(r"C:\Users\DELL\Downloads\2185358-Assignment2-copy (2).pdf")
#x.close()
#x=zipfile.ZipFile("myzipfile.zip")
#x.extractall()
#---------------------------------
"""
# readlines function
f = open("abc.txt", "r")
print(f.readlines(33))
"""


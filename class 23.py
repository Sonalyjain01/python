"""
#create xml file
import xml.etree.ElementTree as xml
def myfile(file):
    r=xml.Element("HOD")
    t=xml.Element("Teacher")
    r.append(t)
    s=xml.SubElement(t,"Sub")
    s.text="python"
    c=xml.SubElement(t,"country")
    c.text="India"

    tree=xml.ElementTree(r)
    with open (file,"wb") as x:
        tree.write(x)
myfile("myxmlfile.xml")
"""
#  use of f-string
a='abc'
b=24
print("value of a is",a)
print(f"value of a and b are {a},{b}")


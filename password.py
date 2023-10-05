
"""
c="""
"""
import random
import string
c=int(input("Enter the length of password: "))
character=string.ascii_letters+string.digits+string.punctuation
p="".join(random.sample(character,c))
print(p)
"""
#qrcode generator
import qrcode
b=qrcode.make("https://drive.google.com/file/d/1t2vrfCQ7VQ02OmunNi2qzPBJf3QUzfTE/view?usp=sharing")
b.save("abc.png")

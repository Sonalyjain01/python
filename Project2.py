"""
import pandas as pd
x=pd.read_html("https://www.bankrate.com/banking/cds/cd-rates/#best-cd-rates-from-top-banks")
#print(x)
#print(type(x),len(x))
#print(x[0])
print(x[12])
"""
"""
#format()
x,y=12,24
print("value of x" ,x, "value of y", y)
print("value of x is {} and the value of y is {} ". format(x,y))
print("value of x is {0} and the value of y is {1} ". format(x,y))
print("value of x is {} and the value of y is {} and sum of x and y is{} ". format(x,y,x+y))
"""
"""    
#import pywhatkit as p
#p.sendwhatmsg("+919639358020","hello testing",16,44,10)

import pywhatkit as p
p.sendwhatmsg("+919639358020","hello ",11,32,10)
"""
"""
import random
a=random.randint(10000,99999)
print(a)
import pywhatkit as p
p.sendwhatmsg("+918266026682","Jai Jinendra{}" .format(a),11,42,10)
"""
"""
import pywhatkit as p
p.sendwhatmsg_instantly("+917906244838","suiiiiiii")
"""
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as m:
    print("speak now............")
    audio=r.listen(m)
    text=r.recognize_google(audio)
    print(text)


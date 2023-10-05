print("---------Welcome to my quiz game----------")
name=input("enter your name :")
print("Welcome :",name)
print("some conditions:")
print("1. There are 5 set of questions .")
print("2. Each set contain at least 5 questions.")
print("3. gave +1 marks for each correct answer and cut 0.25 marks for each wrong answer.")
print("4. passing marks for each set are 3 marks.")
print("5. All questions are mandatory")
score=0
ans=input("Do you want to continue? ").lower()
if ans=="yes":
    print("Start the game")
    print("Set-1 :")
    print("----Python questions----")
    print("1.What is the maximum length of a Python identifier?")
    a1=input("a> 32 b>16 c>128 d>No fixed length is specified")
    if a1== "d" or a1=="No fixed length is specified":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("2.  What will be the output of the following code snippet? print(2*3 + (5 + 6)*(1 + 1))")
    a2=input("a>129 b>121 c>None of these d>8")
    if a2=="a" or a2=="129":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("3.  Which of the following concepts is not a part of Python?")
    a3=input("a>pointers b>Loops c>Dynamic typing d>All of the above")
    if a3=="a" or a3=="pointers":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
        
    print("4. Which of the following types of loops are not supported in Python?")
    a4=input("a>for b>while c>do-while d>None of these")
    if a4=="c" or a4=="do-while":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("5. What will be the output of the following code snippet?")
    print("print('Even' if a % 2 == 0 else 'Odd')")
    a5=input("a>Odd b>Even c>None d>Error")
    if a5=="b" or a5=="Even":
        print("Correct ans")
        score+=1
    else:
        print("wrong ans")
        score-=0.25
    print("your score :",score)
    print("----Reasoning questions-----")
    print("1. If NOIDA is written as OPJEB, then what will be the code for DELHI?")
    a6=input("a>EFMAK b>EFAMK c>EFMIJ d>EFMIK")
    if a6=="c" or a6=="EFMIJ":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("2. If CAT is coded as PATC, JOY is coded as POYJ; similarly the word WING will be coded as ")
    a7=input("a>PIGNW b>PINGW c>PGNIW d>PIWGN")
    if a7=="b" or a7=="PINGW":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("3. Which number should come next in the series 1, 2, 3, 10, _")
    a8=input("a>79 b>99 c>89 d>98")
    if a8=="b" or a8=="99":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("4. Which number is wrong in the series 2, 6, 15, 31, 56, 93?")
    a9=input("a>6 b>31 c>56 d>93")
    if a9=="d" or a9=="93":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("5. If PINK is coded as 1691411, then RED will be coded as -")
    a10=input("a>1963 b>1854 c>1853 d>1954")
    if a10=="b" or a10=="1854":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score=-0.25
    print("your score :",score)
    print("Set-3 :")
    print("-----Operating System-----")
    print("1. Which of the following is not an operating system?")
    a11=input("a>Windows b>Linux c>Oracle d>DOS")
    if a11=="c" or a11=="Oracle":
        print("correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("2. When was the first operating system developed?")
    a12=input("a>1948 b>1949 c>1950 d>1951")
    if a12=="c" or a12=="1950":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("3. Which of the following is the extension of Notepad?")
    a13=input("a>.txt b>.xls c>.ppt d>.bmp")
    if a13=="a" or a13==".txt":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("4. When does page fault occur?")
    a14=input("a>The page is present in memory. b>The deadlock occurs. c>The page does not present in memory. d>The buffering occurs.")
    if a14=="c" or a14=="The page does not present in memory.":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("5. Which is the Linux operating system?")
    a15=input("a>Private operating system b>Windows operating system c>Open-source operating system d>None of these")
    if a15=="c" or a15=="Open-source operating system":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("your score :",score)
    print("Set-4 :")
    print("----Database Management System----")
    print("1. A huge collection of the information or data accumulated form several different sources is known as ________:")
    a16=input("a>Data Management b>Data Mining c>Data Warehouse d>Both B and C")
    if a16=="c" or a16=="Data Warehouse":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("2. Which one of the following refers to the 'data about data'?")
    a17=input("a>Directory b>Sub Data c>Warehouse d>Meta Data")
    if a17=="d" or a17=="Meta data":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("3. To which of the following the term 'DBA' referred?")
    a18=input("a>Data Bank Administrator b>Database Administrator c>Data Administrator d>None of the above")
    if a18=="b" or a18=="Database Administrator":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("4. In general, a file is basically a collection of all related______.")
    a19=input("a>Rows & Columns b>Fields c>Database d>Records")
    if a19=="d" or a19=="Records":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("5. Which of the following refers to the number of tuples in a relation?")
    a20=input("a>Entity b>Column c>Cardinality d>None of the above")
    if a20=="c" or a20=="Cardinality":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("your score :",score)
    print("Set-5 :")
    print("----General Knowledge----")
    print("1. What is the pH value of the human body?")
    a21=input("a>9.2 to 9.8 b>7.0 to 7.8 c>6.1 to 6.3 d>5.4 to 5.6")
    if a21=="b" or a21=="7.0 to 7.8":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("2. Elections to panchayats in state are regulated by")
    a22=input("a>Gram panchayat b>Nagar Nigam c>Election Commission of India d>State Election Commission ")
    if a22=="d" or a22=="State Election Commision":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("3. Forming of Association in India is")
    a23=input("a>Legal Right b>Illegal Right c>Natural Right d>Fundamental Right.")
    if a23=="d" or a23=="Fundamental Right":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("4. Chelaiya Samiti is related to which of the following?")
    a24=input("a>Banking sector b>Insurance sector c>Health Sector d>Tax reforms")
    if a24=="d" or a24=="Tax reforms":
        print("Correct ans")
        score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("5. Which of the given cities is located on the bank of river Ganga?")
    a25=input("a>Patna b>Gwalior c>Bhopal d>Mathura")
    if a25=="a" or a25=="Patna":
         print("Correct ans")
         score+=1
    else:
        print("Wrong ans")
        score-=0.25
    print("your score :",score)
    print("----Quiz Completed----")
    print("Total score :", score)
    if score<18:
        print("Poor, You have to study well")
    elif score<22:
        print("Average")
    else:
        print("Well Done")
else:
    print("Good bye")

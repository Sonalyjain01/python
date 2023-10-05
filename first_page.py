
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo
import os
from tkinter import filedialog
from pygame import mixer
import random
from tkinter import ttk
 
root=tk.Tk()
root.geometry("800x400")
root .title("Fuzzy World")
main_frame=tk.Frame(root)

page_1=tk.Frame(main_frame)
page_1_lb=tk.Label(page_1,text='Home',font=('Bold',20)) 
page_1_lb.pack()
page_1.pack(pady=100)
main_frame.pack(fill=tk.BOTH,expand=True)

def open_music_player():
    # Implement the logic to open the music player here
    open_music_player_window = tk.Toplevel(root)
    open_music_player_window.title("Music Player")
    open_music_player_window.geometry("700x500")

    mixer.init()  # Initialize the mixer

    open_music_player_window.current_file = ""
    open_music_player_window.paused = False

    # Create buttons
    btn_select= tk.Button(
        open_music_player, text="Select File", command=selectFile)
    
    btn_select.pack(pady=10)

    btn_play = tk.Button(open_music_player, text="Play", command=playMusic)
    btn_play.pack(pady=5)

    btn_pause = tk.Button(open_music_player, text="Pause", command=pauseMusic)
    btn_pause.pack(pady=5)

    btn_stop = tk.Button(open_music_player, text="Stop", command=stopMusic)
    btn_stop.pack(pady=5)
        

    def selectFile():
        current_file = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("Audio Files", "*.mp3"),)
        )
        

    def playMusic():
        if current_file != "":
            if paused:
                mixer.music.unpause()
                paused = False
                
            
        else:
            mixer.music.load(current_file)
            mixer.music.play()
        
                
    def pauseMusic():
        if current_file != "":
            if not paused:
                mixer.music.pause()
                paused = True
                
            
        

    def stopMusic():
        if current_file != "":
            mixer.music.stop()
            paused = False
                

    print("Music Player button clicked!")
    
def open_games():
    # Implement the logic to open the games here
    open_games_window = tk.Toplevel(root)
    open_games_window.title("Games")
    
    open_games_window.geometry("700x500")
    open_games_window .title("games")
    main_frame=tk.Frame(open_games_window)

    page_1=tk.Frame(main_frame)
    page_1_lb=tk.Label(page_1,text='Games',font=('Bold',20)) 
    page_1_lb.pack()
    page_1.pack(pady=100)
    main_frame.pack(fill=tk.BOTH,expand=True)

    def open_game_2048():
        # Implement the logic to open the music player here
        open_game_2048_window = tk.Toplevel(root)
        open_game_2048_window.title("2048 Game")
        print("2048 game button clicked!")    
    
    def open_quiz_game():
        # Implement the logic to open the games here
        open_quiz_game_window = tk.Toplevel(root)
        open_quiz_game_window.title("Quiz Game")
        print("Quiz game button clicked!")
    
    def open_memory_puzzle():
        # Implement the logic to open the web browser here
        open_memory_puzzle_window = tk.Toplevel(root)
        open_memory_puzzle_window.title("Memory Puzzle")
        
        tabs = ttk.Notebook(open_memory_puzzle_window) 
        easy= ttk.Frame(tabs)
        def draw(a,l,m):
            global base1
            if a=='A':
                d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='B':
                d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='C':
                d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='D':
                d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='E':
                d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='F':
                d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='G':
                d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='H':
                d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
    
        def quizboard():
            global base1,ans1,board1,moves1
            count=0
            for i in range(4):
                for j in range(4):
                    rec=base1.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
                    if(board1[i][j]!='.'):
                         draw(board1[i][j],i,j)
                         count+=1
            if count==16:
                base1.create_text(200,450,text="No. of moves: "+str(moves1),font=('arial',20))
        
        def call(event):
            global base1,ans1,board1,moves1,prev1
            i=event.x//100
            j=event.y//100
            if board1[i][j]!='.':
                return
            moves1+=1
            #print(moves)
            if(prev1[0]>4):
                 prev1[0]=i
                 prev1[1]=j
                 board1[i][j]=ans1[i][j]
                 quizboard()
            else:
                 board1[i][j]=ans1[i][j]
                 quizboard()
                 if(ans1[i][j]==board1[prev1[0]][prev1[1]]):
                     print("matched")
                     prev1=[100,100]
                     quizboard()
                     return
                 else:
                     board1[prev1[0]][prev1[1]]='.'
                     quizboard()
                     prev1=[i,j]
                     return
 
        base1=Canvas(easy,width=500,height=500)
        base1.pack()
        ans1 = list('AABBCCDDEEFFGGHH')
        random.shuffle(ans1)
        ans1 = [ans1[:4],
                ans1[4:8],
                ans1[8:12],
                ans1[12:]] 
 
        base1.bind("<Button-1>", call)
 
        moves1=IntVar()
        moves1=0
 
        prev1=[100,100]
 
        board1=[list('.'*4) for count in range(4)]
        quizboard()
        open_music_player_window2 = ttk.Frame(tabs)
 
        def draw1(a,l,m):
            global base2
            if a=='A':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='B':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='C':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='D':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='E':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='F':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='G':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='H':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
            elif a=='I':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='J':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='K':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='black')
            elif a=='L':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='orange')
            elif a=='M':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='black')
            elif a=='N':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='orange')
            elif a=='O':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='green')
            elif a=='P':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='black')
            elif a=='Q':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='orange')
            elif a=='R':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='green')
     
    def puzzleboard2():
           global base2,ans2,board2,moves2
           count=0
           for i in range(6):
               for j in range(6):
                   rec=base2.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
                   if(board2[i][j]!='.'):
                       draw1(board2[i][j],i,j)
                       count+=1
           if count>=36:
              base2.create_text(300,650,text="No. of moves: "+str(moves2),font=('arial',20))
    
    def call2(event):
          global base2,ans2,board2,moves2,prev2
          i=event.x//100
          j=event.y//100
          if board2[i][j]!='.':
              return
          moves2+=1
          if(prev2[0]>6):
              prev2[0]=i
              prev2[1]=j
              board2[i][j]=ans2[i][j]
              puzzleboard2()
          else:
              board2[i][j]=ans2[i][j]
              puzzleboard2()
              if(ans2[i][j]==board2[prev2[0]][prev2[1]]):
                  prev2=[100,100]
                  puzzleboard2()
                  return
              else:
                  board2[prev2[0]][prev2[1]]='.'
                  puzzleboard2()
                  prev2=[i,j]
                  return
    
    base2=Canvas(open_music_player_window2 ,width=1000,height=1000)
    base2.pack()
    ans2 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRR')
    random.shuffle(ans2)
    ans2 = [ans2[:6],
            ans2[6:12],
            ans2[12:18],
            ans2[18:24],
            ans2[24:30],
            ans2[30:]
            ]
    base2.bind("<Button-1>", call2)
    moves2=IntVar()
    moves2=0
    prev2=[100,100]
    board2=[list('.'*6) for count in range(6)]
    puzzleboard2()
    open_music_player_window3 = ttk.Frame(tabs)
    tabs.add(easy, text ='Easy')
    tabs.add(open_music_player_window2 , text ='Medium')
    tabs.add(open_music_player_window3 , text ='Hard')
    tabs.pack(expand = 1, fill ="both")
       
    def draw2(a,l,m):
        global base3
        if a=='A':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='red')
        elif a=='B':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='yellow')
        elif a=='C':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='blue')
        elif a=='D':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='red')
        elif a=='E':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='yellow')
        elif a=='F':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='blue')
        elif a=='G':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='red')
        elif a=='H':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='green')
        elif a=='I':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='yellow')
        elif a=='J':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='blue')
        elif a=='K':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='black')
        elif a=='L':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='orange')
        elif a=='M':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='black')
        elif a=='N':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='orange')
        elif a=='O':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='green')
        elif a=='P':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='pink')
        elif a=='Q':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='green')
        elif a=='R':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='pink')
        elif a=='S':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='purple')
        elif a=='T':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='purple')
        elif a=='U':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='purple')
        elif a=='V':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='pink')
        elif a=='W':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='maroon')
        elif a=='X':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='maroon')
        elif a=='Y':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='maroon')
        elif a=='Z':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='brown')
        elif a=='a':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='brown')
        elif a=='b':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='brown')
        elif a=='c':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='aqua')
        elif a=='d':
            d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='aqua')
        elif a=='e':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='aqua')
        elif a=='f':
            d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='magenta')
        elif a=='g':
            d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='magenta')
                
    def quizboard3():
        global base3,ans3,board3,moves3
        count=0
        for i in range(8):
            for j in range(8):
                e=base3.create_rectangle(80*i,j*80,80*i+80,80*j+80,fill="white")
                if(board3[i][j]!='.'):
                    draw2(board3[i][j],i,j)
                    count+=1
        if count>=64:
            base3.create_text(300,650,text="No. of moves: "+str(moves3),font=('arial',20))     
 
    def call3(event):
         global base3,ans3,board3,moves3,prev3
         i=event.x//80
         j=event.y//80
         if board3[i][j]!='.':
             return
         moves3+=1
         if(prev3[0]>8):
             prev3[0]=i
             prev3[1]=j
             board3[i][j]=ans3[i][j]
             quizboard3()
         else:
             board3[i][j]=ans3[i][j]
             quizboard3()
             if(ans3[i][j]==board3[prev3[0]][prev3[1]]):
                 print("matched")
                 prev3=[100,100]
                 quizboard3()
                 return
             else:
                board3[prev3[0]][prev3[1]]='.'
                quizboard3()
                prev3=[i,j]
                return
   
    base3=Canvas(open_music_player_window3 ,width=1000,height=1000)
    base3.pack()

    ans3 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUWWXXYYZZaabbccddeeffgg')
    random.shuffle(ans3)
    ans3 = [ans3[:8],
           ans3[8:16],
           ans3[16:24],
           ans3[24:32],
           ans3[32:40],
           ans3[40:48],
           ans3[48:56],
           ans3[56:]
           ]
    base3.bind("<Button-1>", call3)
    moves3=IntVar()
    moves3=0
    prev3=[80,80]
    board3=[list('.'*8) for count in range(8)]
    quizboard3()
    print("Memory puzzle button clicked!")
    
    def open_snake_game():
         # Implement the logic to open the chatbot here
         print("Snake game button clicked!")

    bottom_frame=tk.Frame(open_games_window)
    game_2048_btn=tk.Button(bottom_frame,text='2048 Game',
                            font=("Bold",12),
                            bg='#1877f2',fg='white',width=12,
                            command=open_game_2048)
    game_2048_btn.pack(side=tk.LEFT,padx=35,pady=20)

    quiz_game_btn=tk.Button(bottom_frame,text='Quiz Game',
                            font=("Bold",12),
                            bg='#1877f2',fg='white',width=12,
                            command=open_quiz_game)
    quiz_game_btn.pack(side=tk.LEFT,padx=35,pady=20)

    memory_puzzle_btn=tk.Button(bottom_frame,text='Memory Puzzle',
                                font=("Bold",12),
                                bg='#1877f2',fg='white',width=12,
                                command=open_memory_puzzle)
    memory_puzzle_btn.pack(side=tk.LEFT,padx=25,pady=20)
       
    snake_game_btn=tk.Button(bottom_frame,text='Snake Game',
                             font=("Bold",12),
                             bg='#1877f2',fg='white',width=12,
                             command=open_snake_game)
                   
    snake_game_btn.pack(side=tk.RIGHT,padx=25,pady=20)

    bottom_frame.pack(side=tk.BOTTOM,pady=55)
    print("Games button clicked!")

def open_web_browser():
    # Implement the logic to open the web browser here
    open_web_browser_window = tk.Toplevel(root)
    open_web_browser_window.title("Web Browser")
    open_web_browser_window.geometry("700x400")
    def open_youtube():
        webbrowser.open("https://www.youtube.com")

    def open_google():
        webbrowser.open("https://www.google.com")

    def open_twitter():
        webbrowser.open("https://www.twitter.com")
    
    def open_facebook():
        webbrowser.open("https://www.facebook.com")

    def open_instagram():
         webbrowser.open("https://www.instagram.com")
   
    def open_whatsapp_web():
        webbrowser.open("https://web.whatsapp.com")
    
    def open_telegram_web():
        webbrowser.open("https://web.telegram.org")

    # Create buttons
    youtube_button = tk.Button(open_web_browser_window, text="YouTube", command=open_youtube,padx=20,width=10)
    youtube_button.pack()

    google_button = tk.Button(open_web_browser_window, text="Google", command=open_google,padx=20,width=10)
    google_button.pack()

    twitter_button = tk.Button(open_web_browser_window, text="Twitter", command=open_twitter,padx=20,width=10)
    twitter_button.pack()

    facebook_button = tk.Button(open_web_browser_window, text="Facebook", command=open_facebook,padx=20,width=10)
    facebook_button.pack()
    
    instagram_button = tk.Button(open_web_browser_window, text="Instagram", command=open_instagram,padx=20,width=10)
    instagram_button.pack()

    whatsapp_web_button = tk.Button(open_web_browser_window, text="WhatsApp Web", command=open_whatsapp_web,padx=20,width=10)
    whatsapp_web_button.pack()

    telegram_web_button = tk.Button(open_web_browser_window, text="Telegram Web", command=open_telegram_web,padx=20,width=10)
    telegram_web_button.pack()

    print("Web Browser button clicked!")

def open_video_player():
    # Implement the logic to open the video player here
    open_video_player_window = tk.Toplevel(root)
    open_video_player_window.title("Video Player")

    open_video_player_window.geometry("600x500")
    open_video_player_window.configure(bg="skyblue")

    lbl1=Label(open_video_player_window,text="Video Player",bg="purple",
               fg="white",font="none 24 bold")
            
    lbl1.config(anchor=CENTER)
    lbl1.pack()

    def openFile():
        file= askopenfile(mode="r",filetypes=[('Video Files',['*.mp4',"*.mov"])])
        if file is not None:
            global filename
            filename=file.name
            global videoplayer
            videoplayer=TkinterVideo(master=open_video_player_window, scaled=True)
            videoplayer.load(r"{}".format(filename))
            videoplayer.pack(expand=True,fill="both" )

    def playFile():
        videoplayer.play()
    
    def stopFile():
        videoplayer.stop()

    def pauseFile():
        videoplayer.pause()
    
    openbtn=Button(open_video_player_window,text="Open",command=lambda:openFile())
    openbtn.pack(side=TOP,pady=6)

    playbtn=Button(open_video_player_window,text="Play",command=lambda:playFile())
    playbtn.pack(side=TOP,pady=6)

    stopbtn=Button(open_video_player_window,text="Stop",command=lambda:stopFile())
    stopbtn.pack(side=TOP,pady=6)

    pausebtn=Button(open_video_player_window,text="Pause",command=lambda:pauseFile())
    pausebtn.pack(side=TOP,pady=6)
    print("Video Player button clicked!")

bottom_frame=tk.Frame(root)
music_player_btn=tk.Button(bottom_frame,text='Music Player',
                   font=("Bold",12),
                   bg='#1877f2',fg='white',width=12,
                   command=open_music_player)
music_player_btn.pack(side=tk.LEFT,padx=35)

video_player_btn=tk.Button(bottom_frame,text='Video Player',
                   font=("Bold",12),
                   bg='#1877f2',fg='white',width=12,
                   command=open_video_player)
video_player_btn.pack(side=tk.LEFT,padx=35)

web_browser_btn=tk.Button(bottom_frame,text='Web Browser',
                   font=("Bold",12),
                   bg='#1877f2',fg='white',width=12,
                   command=open_web_browser)
web_browser_btn.pack(side=tk.RIGHT,padx=35)

games_btn=tk.Button(bottom_frame,text='Games',
                   font=("Bold",12),
                   bg='#1877f2',fg='white',width=12,
                   command=open_games)
games_btn.pack(side=tk.RIGHT,padx=25)

bottom_frame.pack(side=tk.BOTTOM,pady=36,padx=30)
root.mainloop()

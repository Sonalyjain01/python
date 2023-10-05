import tkinter as tk
root=tk.Tk()
root.geometry("700x500")
root .title("games")
main_frame=tk.Frame(root)

page_1=tk.Frame(main_frame)
page_1_lb=tk.Label(page_1,text='Games',font=('Bold',20)) 
page_1_lb.pack()
page_1.pack(pady=100)
main_frame.pack(fill=tk.BOTH,expand=True)

def open_game_2048():
    # Implement the logic to open the music player here
    print("2048 game button clicked!")

def open_quiz_game():
    # Implement the logic to open the games here
    print("Quiz game button clicked!")

def open_memory_puzzle():
    # Implement the logic to open the web browser here
    print("Memory puzzle button clicked!")

def open_snake_game():
    # Implement the logic to open the chatbot here
    print("Snake game button clicked!")

bottom_frame=tk.Frame(root)
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
root.mainloop()


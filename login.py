import tkinter as tk
from tkinter import messagebox

# Sample user database (in a real-world scenario, this should be stored securely)
users = {
    "user1": "password1",
    "user2": "password2"
}

def check_credentials(username, password):
    return username in users and users[username] == password

def login():
    username = entry_username.get()
    password = entry_password.get()

    if check_credentials(username, password):
        messagebox.showinfo("Login Successful", f"Welcome, {username} in the Fuzzy World!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

def sign_up():
    username = entry_new_username.get()
    password = entry_new_password.get()

    if username and password:
        users[username] = password
        messagebox.showinfo("Sign Up Successful", "You have signed up successfully!")
    else:
        messagebox.showerror("Sign Up Failed", "Username and password are required")

# GUI setup
root = tk.Tk()
root.title("Login and Sign-Up")
root.geometry("600x500")
# Login Page
frame_login = tk.Frame(root)
frame_login.pack(padx=20, pady=20)

label_username = tk.Label(frame_login, text="Username:")
label_username.pack()
entry_username = tk.Entry(frame_login)
entry_username.pack()

label_password = tk.Label(frame_login, text="Password:")
label_password.pack()
entry_password = tk.Entry(frame_login, show="*")
entry_password.pack()

btn_login = tk.Button(frame_login, text="Login", command=login)
btn_login.pack()

# Sign-Up Page
frame_signup = tk.Frame(root)
frame_signup.pack(padx=20, pady=20)

label_new_username = tk.Label(frame_signup, text="New Username:")
label_new_username.pack()
entry_new_username = tk.Entry(frame_signup)
entry_new_username.pack()

label_new_password = tk.Label(frame_signup, text="New Password:")
label_new_password.pack()
entry_new_password = tk.Entry(frame_signup, show="*")
entry_new_password.pack()

btn_signup = tk.Button(frame_signup, text="Sign Up", command=sign_up)
btn_signup.pack()

# Show the login page by default
frame_login.tkraise()

# Function to switch between Login and Sign-Up pages
def switch_to_login():
    frame_login.tkraise()

def switch_to_signup():
    frame_signup.tkraise()

# Menu to switch between Login and Sign-Up pages
menu = tk.Menu(root)
root.config(menu=menu)

login_menu = tk.Menu(menu)
menu.add_cascade(label="Login/Sign Up", menu=login_menu)
login_menu.add_command(label="Login", command=switch_to_login)
login_menu.add_command(label="Sign Up", command=switch_to_signup)

root.mainloop()

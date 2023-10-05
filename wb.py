import tkinter as tk
import webbrowser

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

# Create the main window
window = tk.Tk()
window.title("Web Browser")
window.geometry("700x400")

# Create buttons
youtube_button = tk.Button(window, text="YouTube", command=open_youtube,padx=20,width=10)
youtube_button.pack()

google_button = tk.Button(window, text="Google", command=open_google,padx=20,width=10)
google_button.pack()

twitter_button = tk.Button(window, text="Twitter", command=open_twitter,padx=20,width=10)
twitter_button.pack()

facebook_button = tk.Button(window, text="Facebook", command=open_facebook,padx=20,width=10)
facebook_button.pack()

instagram_button = tk.Button(window, text="Instagram", command=open_instagram,padx=20,width=10)
instagram_button.pack()

whatsapp_web_button = tk.Button(window, text="WhatsApp Web", command=open_whatsapp_web,padx=20,width=10)
whatsapp_web_button.pack()

telegram_web_button = tk.Button(window, text="Telegram Web", command=open_telegram_web,padx=20,width=10)
telegram_web_button.pack()



# Start the main loop
window.mainloop()

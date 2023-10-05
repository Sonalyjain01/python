import tkinter as tk
from googlesearch import search

def search_google():
    query = entry.get()
    results.delete('1.0', tk.END)  # Clear previous search results
    for url in search(query, num=5, stop=5):
        results.insert(tk.END, url + '\n')

root = tk.Tk()
root.title("My Google")

label = tk.Label(root, text="Enter your search query:")
label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=search_google)
search_button.pack()

results = tk.Text(root)
results.pack()

root.mainloop()

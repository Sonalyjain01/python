import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("700x500")

        mixer.init()  # Initialize the mixer

        self.current_file = ""
        self.paused = False

        # Create buttons
        self.btn_select = tk.Button(
            self.root, text="Select File", command=self.select_file
        )
        self.btn_select.pack(pady=10)

        self.btn_play = tk.Button(self.root, text="Play", command=self.play_music)
        self.btn_play.pack(pady=5)

        self.btn_pause = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.btn_pause.pack(pady=5)

        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.btn_stop.pack(pady=5)

    def select_file(self):
        self.current_file = filedialog.askopenfilename(
            initialdir="/", title="Select File", filetypes=(("Audio Files", "*.mp3"),)
        )

    def play_music(self):
        if self.current_file != "":
            if self.paused:
                mixer.music.unpause()
                self.paused = False
            else:
                mixer.music.load(self.current_file)
                mixer.music.play()

    def pause_music(self):
        if self.current_file != "":
            if not self.paused:
                mixer.music.pause()
                self.paused = True

    def stop_music(self):
        if self.current_file != "":
            mixer.music.stop()
            self.paused = False

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()

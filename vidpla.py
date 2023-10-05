from tkinter import  *
from tkinter import font
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo
window=Tk()
window.title("Video Player")
window.geometry("600x500")
window.configure(bg="skyblue")

lbl1=Label(window,text="Video Player",bg="purple",
           fg="white",font="none 24 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()

def openFile():
    file= askopenfile(mode="r",filetypes=[('Video Files',['*.mp4',"*.mov"])])
    if file is not None:
        global filename
        filename=file.name
        global videoplayer
        videoplayer=TkinterVideo(master=window, scaled=True)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True,fill="both" )

def playFile():
    videoplayer.play()

def stopFile():
    videoplayer.stop()

def pauseFile():
    videoplayer.pause()

openbtn=Button(window,text="Open",command=lambda:openFile())
openbtn.pack(side=TOP,pady=6)

playbtn=Button(window,text="Play",command=lambda:playFile())
playbtn.pack(side=TOP,pady=6)

stopbtn=Button(window,text="Stop",command=lambda:stopFile())
stopbtn.pack(side=TOP,pady=6)

pausebtn=Button(window,text="Pause",command=lambda:pauseFile())
pausebtn.pack(side=TOP,pady=6)

window.mainloop()

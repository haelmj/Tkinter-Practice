from pytube import YouTube
from tkinter import *
from tkinter import ttk
import os

DEFAULT_PATH = os.path.join( os.getenv('USERPROFILE'), 'Downloads')

window = Tk()
window.wm_title('YouTube Downloader') # set up the title and size.
window.geometry('500x200')  # set up the size
window.resizable(width=True, height=True)

top = Frame(window, width=500, height=50)
top.pack(side=TOP)
bottom = Frame(window, width=500, height=50)
bottom.pack(side=BOTTOM)
left = Frame(window,  width=300, height=100)
left.pack(side=LEFT)
right = Frame(window, width=50, height=100)
right.pack(side=RIGHT)

class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder=placeholder
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"


def download_video():
    yt = YouTube(yt_link.get())
    yt.streams.first().download(DEFAULT_PATH)

style = ttk.Style(window)
style.configure("Placeholder.TEntry", foreground="#d5d5d5")

yt_link = StringVar()
entry = PlaceholderEntry(left, "URL", textvariable=yt_link, width=50)
entry.grid(row=2, column=2, columnspan=4)

file_path = StringVar()
entry2 = PlaceholderEntry(left, "Download Path", textvariable=file_path, width=50)
entry2.grid(row=5, column=2, columnspan=4)

b2 = Button(right, text='Download', width=12, command= download_video)
b2.grid(row=2, column=6)

b1 = Button(right, text='Choose Download Location')
b1.grid(row=5, column=6)

window.mainloop()

"""
Simple GUI YouTube Downloader

"""

from pytube import YouTube
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askdirectory
import os

# get default download folder path
DEFAULT_PATH = os.path.join( os.getenv('USERPROFILE'), 'Downloads')

window = Tk()
# set up the title and size
window.wm_title('YouTube Downloader') 
window.geometry('400x170')  
window.resizable(width=True, height=True)

# top = Frame(window, width=500, height=50)
# top.pack(side=TOP)
# bottom = Frame(window, width=500, height=50)
# bottom.pack(side=BOTTOM)
# left = Frame(window,  width=300, height=100)
# left.pack(side=LEFT)
# right = Frame(window, width=50, height=100)
# right.pack(side=RIGHT)

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
    if file_path.get():
        yt.streams.first().download(file_path.get())
    else:
        entry2.delete(0, END)
        entry2.insert(0, DEFAULT_PATH)
        yt.streams.first().download(DEFAULT_PATH)

def browse_folder():
    try:
        folder_path = askdirectory()
        entry2.delete(0, END)
        entry2.insert(0,folder_path)
    except Exception:
        entry2.delete(0, END)
        entry2.insert(0, DEFAULT_PATH)


style = ttk.Style(window)
style.configure("Placeholder.TEntry", foreground="#d5d5d5")

yt_link = StringVar()
entry = PlaceholderEntry(window, "Youtube Link", textvariable=yt_link, width=50)
entry.grid(row=2, column=2, columnspan=4, padx=5, pady=5)

l1 = Label(window, text='----------')
l1.grid(row=3, column =2, columnspan=4)

file_path = StringVar()
entry2 = PlaceholderEntry(window, "Destination Path", textvariable=file_path, width=50)
entry2.grid(row=5, column=2, columnspan=4)

b2 = Button(window, text='Download', width=12, command= download_video)
b2.grid(row=2, column=6, pady=5)

b1 = Button(window, text='Browse Folder', command=browse_folder)
b1.grid(row=5, column=6)

window.mainloop()

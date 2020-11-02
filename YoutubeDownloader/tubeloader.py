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
window.geometry('415x170')  
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

def progress_check(chunk, file_handle, bytes_remaining):
    # get percentage of file downloaded
    percent = (100*(file_size - bytes_remaining))/file_size
    print("{:00.0f}% downloaded".format(percent))

def entry_reset(stream, file_handle):
    entry.delete(0, END)

def download_video():
    try:
        video = YouTube(yt_link.get(), on_progress_callback=progress_check,on_complete_callback=entry_reset)
        if file_path.get():
            folder_path = file_path.get()
        else:
            entry2.delete(0, END)
            entry2.insert(0, DEFAULT_PATH)
            folder_path = DEFAULT_PATH
        video_stream = video.streams.first()
        global file_size
        file_size = video_stream.filesize
        video_stream.download(folder_path)
    except Exception as e:
        print(e)

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

download_type = IntVar()
rd_btn = Radiobutton(window, text='Video', padx=20, variable=download_type, value=1)
rd_btn.grid(row=3, column=2)

rd_btn2 = Radiobutton(window, text='Playlist', padx=20, variable=download_type, value=2)
rd_btn2.grid(row=3, column=3)


l1 = Label(window, text='----------')
l1.grid(row=4, column =2, columnspan=4)

file_path = StringVar()
entry2 = PlaceholderEntry(window, "Destination Path", textvariable=file_path, width=50)
entry2.grid(row=5, column=2, columnspan=4)

b2 = Button(window, text='Download', width=12, command= download_video)
b2.grid(row=2, column=6, pady=5)

b1 = Button(window, text='Browse Folder', command=browse_folder)
b1.grid(row=5, column=6)

window.mainloop()

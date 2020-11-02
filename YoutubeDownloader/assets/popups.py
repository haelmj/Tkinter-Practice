from tkinter import Tk
import tkinter.messagebox as messagebox

def show_info(head, prompt):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(head, prompt)

def show_error(head, prompt):
    root = Tk()
    root.withdraw()
    messagebox.showerror(head, prompt)

def show_warning(head, prompt):
    root = Tk()
    root.withdraw()
    messagebox.showwarning(head, prompt)


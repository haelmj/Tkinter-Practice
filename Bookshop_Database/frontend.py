"""
A program that stores book information:
Title, Author, Year, ISBN

User can: 
-View all books
-Search an entry
-Add an entry
-Update entry
-Delete
-Close
"""
from tkinter import *
from backend import *


window = Tk()
window.wm_title('BookStore')

# functions
def get_selected_row(event):
    try:
        global selected_row
        index=list1.curselection()[0]
        selected_row=list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_row[1])
        e2.delete(0,END)
        e2.insert(END, selected_row[3])
        e3.delete(0,END)
        e3.insert(END, selected_row[2])
        e4.delete(0,END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in search(title_text.get(), author_text.get(), year_text.get(),isbn_text.get()):
        list.insert(END, row)

def insert_command():
    insert(title_text.get(), author_text.get(), year_text.get(),isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(),isbn_text.get()))

def delete_command():
    delete(selected_row[0])
    view_command()

def update_command():
    update(selected_row[0],title_text.get(), author_text.get(), year_text.get(),isbn_text.get())
    view_command()
    

def exit_command():
    window.destroy()
    pass

# create labels at the top

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Year')
l2.grid(row=1, column=0)

l3 = Label(window, text='Author')
l3.grid(row=0, column=2)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

# create entries
title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

year_text=StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=1, column=1)

author_text=StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(row=0, column=3)

isbn_text=StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# list box
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# scroll bar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# link scrollbar to list box
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# buttons
b1 = Button(window, text='View all', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search entry',width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add entry', width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete',width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close',width=12, command=exit_command)
b6.grid(row=7, column=3)

window.mainloop()
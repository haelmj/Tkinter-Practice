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

window = Tk()
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
e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value=StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=1, column=1)

e3_value=StringVar()
e3 = Entry(window, textvariable=e3_value)
e3.grid(row=0, column=3)

e4_value=StringVar()
e4 = Entry(window, textvariable=e4_value)
e4.grid(row=1, column=3)

#create buttons
b1 = Button(window, text='View all')
b1.grid(row=2, column=3)

b2 = Button(window, text='Search entry')
b2.grid(row=3, column=3)

b3 = Button(window, text='Add entry')
b3.grid(row=4, column=3)

b4 = Button(window, text='Update')
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete')
b5.grid(row=6, column=3)

b6 = Button(window, text='Close')
b6.grid(row=7, column=3)
window.mainloop()
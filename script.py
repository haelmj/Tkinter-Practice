from tkinter import * 

# Create an empty Tkinter window
window=Tk()

# def km_to_miles():
#     miles=int(e1_value.get())*1.6
#     t1.insert(END, (f'{miles} miles'))

def kg_converter():
    # Get user value from input box
    kg = int(e1_value.get())

    # converts user value to various units
    grams = kg*1000
    pounds = kg*2.20462
    ounces= kg*35.274

    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)
    t1.insert(END, (f'{grams} grams'))
    t2.delete("1.0", END)
    t2.insert(END, (f'{pounds} pounds'))
    t3.delete("1.0", END)
    t3.insert(END, (f'{ounces} ounces'))

# Create a button widget
# The kg_converter() function is called when the button is push
b1=Button(window, text='Convert', command=kg_converter)
b1.grid(row=0, column=2)

e1_value= StringVar() # Create a special StringVar object
e1 = Entry(window, textvariable=e1_value) # Create an Entry box for user
e1.grid(row=0, column=1)

# Create a Label widget with "Input Kg" as label
l1 = Label(window, text='Input Kg')
l1.grid(row=0, column=0)

# Create three empty text boxes, t1, t2, and t3
t1=Text(window, height=1, width = 20)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width = 20)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width = 20)
t3.grid(row=1, column=2)

# This makes sure to keep the main window open
window.mainloop()
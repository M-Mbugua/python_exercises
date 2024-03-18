# Question: Create a program that asks the user to submit a
# string or number through a graphical user interface (GUI),
# and that string or number is stored as a new line in an existing
# text file. Please have three buttons: Add Line , Save Changes ,
# and Save and Close .

from tkinter import *

root = Tk()

f = open('user_data_gui.txt', 'a+')

user_input = StringVar()
entry = Entry(root, textvariable = user_input)
entry.grid(column = 0, row = 0)

def add():
    f.write(user_input.get() + '\n')
    entry.delete(0, END)

def save():
    global f
    f.close()
    f = open('user_data_gui.txt', 'a+')

def close():
    f.close()
    root.destroy()

btn_add = Button(root, text = "Add Line" , command = add)
btn_add.grid(column = 1, row = 0)

btn_save = Button(root, text = "Save Changes" , command = save)
btn_save.grid(column = 2, row = 0)

btn_close = Button(root, text = "Save and Close" , command = close)
btn_close.grid(column = 3, row = 0)

root.mainloop()




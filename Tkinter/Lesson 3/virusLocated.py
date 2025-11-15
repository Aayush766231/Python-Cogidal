from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('100x100')
root.title('Scan For Virus')

def buttonClick():
    messagebox.showwarning("Alert", 'There is a virus in your system!')
virusButton = Button(text= 'Scan for Virus?', command=buttonClick)

virusButton.place(x=20, y=30)
root.mainloop()
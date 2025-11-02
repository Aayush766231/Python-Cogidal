from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with widgets")
root.geometry('400x300')

lbl = Label(text= "Hey There!", fg = "white", bg = "#072F5F", height= 1, width= 300)
nameLbl = Label(text= "Full Name", bg = "#3895D3")
nameEntry = Entry()

def display():
    name = nameEntry.get()
    global message 
    message = "Welcome to the Application! \n Today's date is "
    greet = "Hello " + name + "\n"
    textBox.insert(END, greet)
    textBox.insert(END, message)
    textBox.insert(END, date.today())

textBox = Text(height=3)
btn = Button(text= "Begin", command= display, height=1, bg= '#1261A0', fg = "white")
fillSpace = Label(text= "Thank you for using this application today!", fg= 'white', bg= 'darkblue', height=11, width=300)

lbl.pack()
nameLbl.pack()
nameEntry.pack()
btn.pack()
textBox.pack()
fillSpace.pack()

root.mainloop()
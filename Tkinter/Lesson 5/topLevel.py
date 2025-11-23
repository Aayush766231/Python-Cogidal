from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('Main Window')

l = Label(root, fg='black', text='This is a main window')

def topWindow():
    top = Toplevel()
    top.title('Top Level')
    top.geometry('100x100')

    l2 = Label(top, text='This is a top window')
    l2.pack()
    top.mainloop()

btn = Button(root, text='Click to open a top window', command=topWindow)
l.pack()
btn.pack()

root.mainloop()
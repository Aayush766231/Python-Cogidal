from tkinter import *

root = Tk()
root.geometry('100x100')
root.title('Event Handling')

def handleKeyPress(event):
    print(event.char)

root.bind('Key', handleKeyPress)

def btnClicked():
    print("The button has been clicked")
btn = Button(text='Click Here')
btn.pack()
btn.bind('Click', btnClicked)

root.mainloop()
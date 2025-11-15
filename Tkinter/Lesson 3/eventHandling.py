from tkinter import *

window = Tk()
window.geometry('100x100')
window.title('Click the Button')

btn = Button(text="Click Here!")
def handleButtonPress(event):
    print('Button was pressed')
btn.bind("<Button-1>", handleButtonPress)

def handleKeyPress(event):
    print(event.char)
window.bind("<Key>", handleKeyPress)

btn.pack()
window.mainloop()
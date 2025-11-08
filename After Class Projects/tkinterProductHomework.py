from tkinter import *

window = Tk()
window.title('Multiplication via tKinter')
window.geometry('400x300')
window.configure(bg = 'darkgray')

lbl = Label(text= 'Hello!', fg= 'white', bg= 'black', height=1, width=300)
num1Lbl = Label(text= 'Enter first number', fg = 'white', bg = 'gray', height=1, width=300)
numEntry1 = Entry()
numEntry1.focus_set()

num2Lbl = Label(text= 'Enter second number here', fg = 'white', bg = 'gray', height=1, width=300)
numEntry2 = Entry()

def display():
    try:
        num1 = numEntry1.get()
        num2 = numEntry2.get()
        global product
        product = float(num1) * float(num2)
        textBox.insert(END, f'{num1} times {num2} is {product} \n')
        numEntry1.delete(0, END)
        numEntry2.delete(0, END)
        numEntry1.focus_set()
    except ValueError:
        textBox.insert(END, 'Please enter valid numbers')

textBox = Text(height=11)
button = Button(text= 'Click to Multiply!', height=1, fg = 'white', bg = 'black', command= display)

numEntry1.bind('<Return>', lambda numEntry: numEntry2.focus_set())

lbl.pack()
num1Lbl.pack()
numEntry1.pack()
num2Lbl.pack()
numEntry2.pack()
button.pack()
textBox.pack()

window.mainloop()
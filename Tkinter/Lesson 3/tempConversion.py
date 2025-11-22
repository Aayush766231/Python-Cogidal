from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x300')
window.title("Temperature Conversion")
frame1 = Frame(master=window, bg='lightblue', height=150, width=400)

tempNumLbl = Label(master=frame1, text="Enter the temperature outside right now", bg='lightblue', fg='black')
tempNum = Entry(master=frame1)

def conversion():
    textBox.delete(1.0, END)
    temp = float(tempNum.get())
    global answer
    answer = messagebox.askquestion('Original Unit', 'Is the original unit Celsius?')
    if answer == 'yes':
        textBox.insert(END, f'{temp} degrees Celsius is ')
        temp *= 1.8
        temp += 32
        textBox.insert(END, f'{temp} degrees Farenheit')
    else:
        textBox.insert(END, f'{temp} degrees Farenheit is ')
        temp -= 32
        temp /= 1.8
        textBox.insert(END, f'{temp} degrees Celsius')
labelButton = Button(text= 'What is the original unit of measurement?', command=conversion)

textBox = Text(fg = 'darkblue', bg = 'pink')

frame1.pack()
tempNumLbl.place(x=25, y=100)
tempNum.place(x=250, y=100)
labelButton.pack()
textBox.pack()

window.mainloop()
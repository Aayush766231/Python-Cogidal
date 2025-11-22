from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x400')
window.title("Length Converter App")
frame1 = Frame(master=window, bg='purple', height=150, width=400)

descLbl = Label(master=frame1, text= 'A conversion calculator between inches and cm', bg='purple', fg='lightblue', font= ("Times New Roman", 15, 'bold'))

lengthNumLbl = Label(master=frame1, text="Enter the length you wish converted:", bg='purple', fg='white')
lengthNum = Entry(master=frame1)

def conversion():
    textBox.delete(1.0, END)
    length = float(lengthNum.get())
    global answer
    answer = messagebox.askquestion('Original Unit', 'Is the original unit inches?')
    if answer == 'yes':
        textBox.insert(END, f'{length} inches is ')
        length *= 2.54
        textBox.insert(END, f'{length} cm')
    else:
        textBox.insert(END, f'{length} cm is ')
        length /= 2.54
        textBox.insert(END, f'{length} inches')
labelButton = Button(text= 'What is the original unit of measurement?', command=conversion)

textBox = Text(fg = 'lightblue', bg = 'darkblue')

frame1.pack()
descLbl.place(x=0, y= 50)
lengthNumLbl.place(x=25, y=100)
lengthNum.place(x=225, y=100)
labelButton.pack()
textBox.pack()

window.mainloop()
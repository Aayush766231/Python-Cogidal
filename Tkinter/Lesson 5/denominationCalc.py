from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Calculator')
root.geometry('500x600')
root.configure(bg='lightblue')

upload = Image.open('money.png.png')

upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
imageLabel = Label(root, image = image, bg = 'light blue')
imageLabel.place(x=100, y=100)

introLabel = Label(root, text= 'Hello! Welcome to the Denomination Calculator', bg='light blue', font=('Times New Roman', 16))
introLabel.place(relx=0.5, y=450, anchor=CENTER)

#shift to new screen, roughly
def calculator():
    calc = Frame(root, bg='lightblue', height=600, width=500)
    calc.pack()

    numericalLabel = Label(calc, bg='lightblue', font=("Times New Roman", 11, 'bold'), text='Enter original number:')
    numericalLabel.place(relx=0.18, rely=.3)

    originalNum = Entry(calc)
    originalNum.place(relx=0.5, rely = 0.3)

    def calculation():
        try:
            thousandAnswer.delete(1.0, END)
            fiveAnswer.delete(1.0, END)
            oneAnswer.delete(1.0, END)

            number = int(originalNum.get())
            number2 = number // 2000
            thousandAnswer.insert(END, number2)

            number -= (number2 * 2000)
            number5 = number // 500
            fiveAnswer.insert(END, number5)
            
            number -= (number5 * 500)
            oneAnswer.insert(END, number // 100)
        except:
            messagebox.showerror('Invalid Number', 'Please enter a valid number')
    
    calculationButton = Button(calc, text='Perform Calculation', command=calculation)
    calculationButton.place(relx = .4, rely = .5)

    thousandLabel = Label(calc, bg='lightblue', font=("Times New Roman", 11, 'bold'), text='2000s notes:')
    thousandLabel.place(relx = 0.3, rely = .6)
    thousandAnswer = Text(calc, height=1, width=15)
    thousandAnswer.place(relx=0.5, rely = 0.6)

    fivehundredLabel = Label(calc, bg='lightblue', font=("Times New Roman", 11, 'bold'), text='500s notes:')
    fivehundredLabel.place(relx = 0.3, rely = 0.7)
    fiveAnswer = Text(calc, height=1, width=15)
    fiveAnswer.place(relx=.5, rely = 0.7)

    hundredLabel = Label(calc, bg='lightblue', font=("Times New Roman", 11, 'bold'), text='100s notes:')
    hundredLabel.place(relx = 0.3, rely = 0.8)
    oneAnswer = Text(calc, height=1, width=15)
    oneAnswer.place(relx=.5, rely = 0.8)

btn = Button(text='Begin', command=calculator)
btn.place(relx=0.5, y=500, anchor=CENTER)


root.mainloop()
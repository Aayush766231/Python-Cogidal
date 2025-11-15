from tkinter import *
from datetime import date

root = Tk()
root.geometry('400x400')
root.title("Age Calculator")
frame1 = Frame(master=root, height=200, width=400, bg = 'white')

nameLbl = Label(master=frame1, height=1, width=10, text='Enter Name:', fg='white', bg='darkblue')
name = Entry(master=frame1)

yearBornLbl = Label(master=frame1,text="Year of Birth", height=1, width=10, bg='darkblue', fg='white')
yearBorn = Entry(master=frame1)

monthBornLbl = Label(master=frame1,text="Birth Month #", height=1, width=10, bg='darkblue', fg='white')
monthBorn = Entry(master=frame1)

dateBornLbl = Label(master=frame1,text='Date of Birth', height=1, width=10, bg='darkblue', fg='white')
dateBorn = Entry(master=frame1)

#button
def display():
    #age calculation
    currentDate = date.today()
    birthYear = yearBorn.get()
    birthMonth = monthBorn.get()
    birthDate = dateBorn.get()
    global currentAge
    currentAge = currentDate.year - float(birthYear) 
    if (float(birthMonth), float(birthDate)) > (currentDate.month, currentDate.day):
        currentAge -= 1
    textBox.delete(1.0, END)
    textBox.insert(END, f'{name.get()}, your age is {int(currentAge)} right now')
btn = Button(master = root, text='Click to find age', height=1, fg='white', bg = 'black', command=display)
#text box
textBox = Text(height=5)

frame1.pack()
nameLbl.place(x=50, y=0)
name.place(x=200, y=0)
yearBornLbl.place(x=50, y=50)
yearBorn.place(x=200, y=50)
monthBornLbl.place(x=50, y=100)
monthBorn.place(x=200, y=100)
dateBornLbl.place(x=50, y=150)
dateBorn.place(x=200, y=150)
btn.pack()
textBox.pack()

root.mainloop()
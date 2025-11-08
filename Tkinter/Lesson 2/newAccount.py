from tkinter import *

root = Tk()
root.title('New Account')
root.geometry('400x300')

frame1 = Frame(master=root, height=200, width=360, bg='#d0efff')
#widget time
nameLabel = Label(master=frame1, height=1, width=10, text='Full Name', bg='blue', fg='white')
emailLabel = Label(master=frame1, height=1, width=10, text='Email Address', bg='blue', fg='white')
passwordLabel = Label(master=frame1, height=1, width=10, text='Enter Password', bg='blue', fg='white')

#input
nameEntry = Entry(master=frame1)
emailEntry = Entry(master=frame1)
passwordEntry = Entry(master=frame1)

#button
def display():
    textBox.insert(END, "Congrats on creating a new account!")
goButton = Button(master=root, text='Create Account', bg='darkblue', fg='white', height=3, width=10, command=display)

#textBox
textBox = Text(master=root, height=3)

#putting everything together
frame1.pack()
nameLabel.place(x=50, y=50)
nameEntry.place(x=150, y=50)
emailLabel.place(x=50, y=100)
emailEntry.place(x=150, y=100)
passwordLabel.place(x=50, y=150)
passwordEntry.place(x=150, y=150)
goButton.pack()
textBox.pack()

root.mainloop()
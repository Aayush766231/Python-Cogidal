from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Password Strength Check')

header = Label(root, text='PASSWORD CHECKER', font=('Calibri', 16, 'bold'))
directions = Label(root, text='Enter password below')
passwordEnter = Entry()
result = Label(root, font=('Times New Roman', 12))

info = Toplevel()
info.title('Information')
info.geometry('300x100')
information = Label(info, text="This checks the strength of your password")
directions1 = Label(info, text='Password must be at least 10 character long')
information.pack()
directions1.pack()

def check(_):
    password = passwordEnter.get()
    if len(password) >= 10:
        result.config(text="")
        strength = 0
        for i in password:
            if 65 <= ord(i) <= 90:
                strength += 2
            elif 97 <= ord(i) <= 122:
                strength += 1
            elif 48 <= ord(i) <= 57:
                strength += 3
            else:
                strength += 5
        if strength > 25:
            result.config(text="Strong Password 👍")
            root.config(bg='green')
            header.config(bg='green')
            directions.config(bg='green')
            result.config(bg='green')
        elif strength > 15:
            result.config(text="Not Strong Enough")
            root.config(bg='yellow')
            header.config(bg='yellow')
            directions.config(bg='yellow')
            result.config(bg='yellow')
        else:
            result.config(text="Weak Password 👎")
            root.config(bg='red')
            header.config(bg='red')
            directions.config(bg='red')
            result.config(bg='red')
passwordEnter.bind("<KeyRelease>", check)

header.pack()
directions.pack()
passwordEnter.pack()
result.pack()

root.mainloop()
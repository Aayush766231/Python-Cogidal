from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.title('Interest Calculator App')
root.configure(bg='lightgreen')

root.rowconfigure(0, weight=1, minsize=200)
root.rowconfigure(1, weight=1, minsize=200)

root.columnconfigure(0, weight=1, minsize=(400/3))
root.columnconfigure(1, weight=1, minsize=(400/3))
root.columnconfigure(2, weight=1, minsize=(400/3))

principalFrame = Frame(root, bg = 'lightblue', relief=GROOVE, bd=2)
principleLabel = Label(principalFrame, text='Principal Amount', bg='lightblue', fg='black', font=('Times New Roman', 8))
principalAmount = Entry(principalFrame)

timeFrame = Frame(root, bg='lightblue', relief=GROOVE, bd=2)
timeLabel = Label(timeFrame, text='Years', bg='lightblue', fg='black', font=('Times New Roman', 8))
timeAmount = Entry(timeFrame)

rateFrame = Frame(root, bg='lightblue', relief=GROOVE, bd=2)
rateLabel = Label(rateFrame, text="Interest Rate", bg='lightblue', fg='black', font=('Times New Roman', 8))
rateAmount = Entry(rateFrame)

bottomFrame = Frame(root, bg='lightblue', relief=GROOVE, bd=2)
def action():
    try:
        principal = float(principalAmount.get())
        time = float(timeAmount.get())
        rate = float(rateAmount.get()) / 100
        display.delete(1.0, END)
        #simple calculation
        simpleInterest = principal*time*rate
        display.insert(END, f'The simple interest is {simpleInterest} \n')
        simpleFinal = principal + simpleInterest
        display.insert(END, f'The total payment using simple interest is {simpleFinal} \n')
        #compound calculation
        compoundInterest = principal*((1+rate)**time) - principal
        display.insert(END, f'\n The compound interest is {compoundInterest} \n')
        compoundFinal = compoundInterest + principal
        display.insert(END, f'The total payment using compound interest is {compoundFinal}')
    except:
        messagebox.showerror('Invalid Input', 'Please enter valid numbers')
actionButton = Button(bottomFrame, text="Compute", command=action)
display = Text(bottomFrame, height=10, width=50)

principalFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
timeFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
rateFrame.grid(row=0, column=2, sticky="nsew",padx=5, pady=5)
bottomFrame.grid(row=1, column=0, columnspan=3, sticky="nsew")

principleLabel.pack(pady=5)
principalAmount.pack(pady=10)
timeLabel.pack(pady=5)
timeAmount.pack(pady=10)
rateLabel.pack(pady=5)
rateAmount.pack(pady=10)
actionButton.pack(pady=5)
display.pack(fill="both", expand=True, padx= 10, pady=10)

root.mainloop()
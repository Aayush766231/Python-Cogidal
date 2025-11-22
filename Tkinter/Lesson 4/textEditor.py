from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

root = Tk()
root.geometry('600x500')
root.title('Text Editor')
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

def openFile():
    filepath = askopenfilename(filetypes= [
        ("Text Files", "*.txt"), ("All Files", "*.*")
    ])
    if not filepath:
        return
    txtBox.delete(1.0, END)
    with open(filepath, 'r') as inputFile:
        text = inputFile.read()
        txtBox.insert(END, text)
        inputFile.close()
    root.title(f'Text Editor -- {filepath}')

def saveFile():
    filepath = asksaveasfilename(defaultextension= 'txt', filetypes=[
        ("Text Files", "*.txt"), ("All Files", "*.*")
    ])
    if not filepath:
        return
    with open(filepath, 'w') as outputFile:
        text = txtBox.get(1.0, END)
        outputFile.write(text)
    root.title(f'Text Editor - {filepath}')

txtBox = Text(root)
buttonFrame = Frame(master=root, relief= RAISED, bd=2)
openButton = Button(master=buttonFrame, text='Open File', command=openFile)
saveButton = Button(master=buttonFrame, text='Save As...', command=saveFile)

openButton.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
saveButton.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

buttonFrame.grid(row=0, column=0, sticky='ns')
txtBox.grid(row=0, column=1, sticky='nsew')

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantManagement:
    def __init__(self, root):
        self.root = root
        self.root.title = ('Restaurant Manager App')

        self.menuItems = {
            "FRIES" : 2,
            "BURGER COMBO" : 3,
            "LUNCH COMBO" : 5,
            "PIZZA COMBO" : 4,
            "CHEESEBURGER" : 2.5,
            "DRINKS" : 2
        }
        self.exchangeRate = 82

        self.setupBackground(root)

        frame = ttk.Frame(root)
        frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

        ttk.Label(frame, text='Restaurant Menu', font=('Arial', 20, 'bold')).grid(
            row=0, columnspan=3, padx=10, pady=10
        )

        self.menuLabels={}
        self.menuQuantities = {}

        for i, (item, price) in enumerate(self.menuItems.items(), start=1):
            label = ttk.Label(frame, text=f"{item} ({price})", font=('Arial', 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menuLabels[item] = label

            quantityEntry = ttk.Entry(frame, width=5)
            quantityEntry.grid(row=i, column=1, padx=10, pady=5)
            self.menuQuantities[item] = quantityEntry
        
        self.currencyVar = tk.StringVar()
        ttk.Label(frame, text='Currency', font=('Arial', 12)).grid(
            row=len(self.menuItems) + 1, column=0, padx=10, pady=5
        )
        currencyDropdown = ttk.Combobox(frame, textvariable=self.currencyVar, state='readonly', width=18, values=('USD', 'INR'))
        currencyDropdown.grid(row=len(self.menuItems) + 1, column=1, padx=10, pady=5)
        currencyDropdown.current(0)
        self.currencyVar.trace('w', self.updateMenuPrices)

        orderButton = ttk.Button(frame, text='Place Order', command=self.placeOrder)
        orderButton.grid(row=len(self.menuItems) + 2, columnspan=3, padx=10, pady=10)

    def setupBackground(self, root):
        bgWidth, bgHeight = 800, 600
        canvas = tk.Canvas(root, width=bgWidth, height=bgHeight)
        canvas.pack()
        originalImage = tk.PhotoImage(file='background.png')
        bgImage = originalImage.subsample(originalImage.width() // bgWidth, originalImage.height() // bgHeight)
        canvas.create_image(0, 0, anchor = tk.NW, image = bgImage)
        canvas.image = bgImage
    def updateMenuPrices(self, *args):
        currency = self.currencyVar.get()
        symbol = '₹' if currency == 'INR' else '$'
        rate = self.exchangeRate if currency == 'INR' else 1
        for item, label in self.menuLabels.items():
            price = self.menuItems[item] * rate
            label.config(text = f'{item} ({symbol}{price})')
    def placeOrder(self):
        totalCost = 0
        orderSummary = 'Order Summary:\n'
        currency = self.currencyVar.get()
        symbol = '₹' if currency == 'INR' else '$'
        rate = self.exchangeRate if currency == 'INR' else 1
        for item, entry in self.menuQuantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menuItems[item] * rate
                cost = quantity*price
                totalCost += cost
                if quantity > 0:
                    orderSummary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
        if totalCost > 0:
            orderSummary += f"\nTotal Cost is {symbol}{totalCost}"
            messagebox.showinfo('Order Placed', orderSummary)
        else:
            messagebox.showerror('Error', "Please order at least one item")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x600')
    app = RestaurantManagement(root)
    root.mainloop()
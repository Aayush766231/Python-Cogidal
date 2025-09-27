class price:
    def __init__(self):
        self.__maxPrice = 900
    def sell(self):
        print("Selling price is {}".format(self.__maxPrice))
    def setMaxPrice(self, price):
        self.__maxPrice = price
        self.sell()

# initialize a new object within the price class and display its value
c = price()
c.sell()
# try to change value of object --> doesn't work (can't change value of private vars from outside)
c.__maxPrice = 1000
c.sell()
# change value of object with respective method and display
c.setMaxPrice(1000)

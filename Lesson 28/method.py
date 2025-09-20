class IOString():
    def __init__(self):
        self.str1 = ""
    def getString(self):
        self.str1 = input("Enter a string: ")
    def stringUpper(self):
        print("Result is:", self.str1.upper())

str1 = IOString()

str1.getString()
str1.stringUpper()
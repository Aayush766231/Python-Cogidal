class stringOriginal:
    def __init__(self, s):
        self.__s = s
    def reverse(self):
        return self.__s[::-1]

strInput = stringOriginal("Hello")
print(strInput.reverse())

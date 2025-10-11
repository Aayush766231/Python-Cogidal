class stringOriginal:
    def __init__(self, s):
        self.__s = s
    def reverse(self):
        self.__s += " "
        reversedList = []
        newString = ""
        for i in self.__s:
            if i.isalnum():
                reversedList.append(i)
            else:
                for j in reversed(reversedList):
                    newString += j
                newString += i
                reversedList.clear()
        return newString.strip()
    
strInput = input("Enter a string: ")
originalStr = stringOriginal(strInput)
print(originalStr.reverse())

class myClass:
    __privateVar = 27

    def __privMethod(self):
        print("Going inside myClass")
    def hello(self):
        print("Private variable:", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMethod()
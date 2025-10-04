class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if self.a < other.a:
            return f"{self.a} is less than {other.a}"
        else:
            return f"{self.a} is not less than {other.a}"
    def __eq__(self, other):
        if self.a == other.a:
            return f"{self.a} is equal to {other.a}"
        else:
            return f"{self.a} not equal to {other.a}"

print("Enter 4 values for comparison:")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
ob1 = A(num1)
ob2 = A(num2)
print(ob1 < ob2)
ob3 = A(num3)
ob4 = A(num4)
print(ob3 == ob4)
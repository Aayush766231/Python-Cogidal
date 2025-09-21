class bankAccount():
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
    def moneyChange(self, type):
        self.type = type.upper()
        if self.type == "WITHDRAW":
            withdrawal = float(input("How much do you wish to withdraw? "))
            if withdrawal < self.balance:
                return self.balance - withdrawal
            else:
                return "You don't have that much money :("
        elif self.type == "DEPOSIT":
            deposit = float(input("How much are you putting in? "))
            return self.balance + deposit

myAccount = bankAccount(1035, 965.32)
print(f"Your new balance is ${myAccount.moneyChange("deposit")}")

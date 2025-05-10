class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
        print("Account Created")

    def debit(self, amt):
        if amt > self.balance:
            print("Debit amount exceeding account balance")
        else:
            self.balance -= amt
            print(f"Updated balance: {self.balance} after debit of acc_no: {self.acc_no}")

    def credit(self, deposit_amt):
        self.balance += deposit_amt
        print(f"Updated balance: {self.balance} after credit of acc_no: {self.acc_no}")

    def print_bal(self):
        print(f"Available balance is: {self.balance} of acc_no: {self.acc_no}")


# Main driver code
init_bal = int(input("Enter initial balance (int): "))
accountNo = int(input("Enter account no: "))

a1 = Account(init_bal, accountNo)

a1.debit(10000)
a1.credit(1001)
a1.print_bal()

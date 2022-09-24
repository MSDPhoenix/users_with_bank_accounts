class BankAccount:
    all_accounts = []
    def __init__(self,int_rate,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self,amount):
        print(f"Depositing ${amount}")
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance > 0:
            self.balance -= amount
            print(f"Withdrawing ${amount}")
            if self.balance < amount:
                print("Insufficient funds.  Charging $5 fee.")
                self.balance -= 5
        else:
            print("Insufficient funds. Transaction cancelled")
        return self

    def display_account_info(self):
        print(f"Interest rate: {self.int_rate}")
        print(f"Balance: {self.balance}\n")
        return self

    def yield_interest(self):
        x = self.balance * self.int_rate
        self.balance += x
        print(f"Interest: {x}, new balance: {self.balance}")
        return self

    @classmethod
    def print_all(cls):
        for account in BankAccount.all_accounts:
            account.display_account_info()

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.accounts = {
            "checking" : BankAccount(.02),
            "savings" : BankAccount(.03)
        }

    def make_deposit(self,amount,user_account):
        self.accounts[user_account].deposit(amount)
        return self

    def make_withdrawal(self,amount,user_account):
        self.accounts[user_account].withdraw(amount)
        return self

    def display_user_balance(self):
        print("Name = ",self.name)
        print("Email = ",self.email)
        for account in self.accounts.values():
            account.display_account_info()
        return self

    def transfer_money(self,amount,other_user):
        if self.accounts["checking"].balance > amount:
            self.accounts["checking"].balance -= amount
            other_user.accounts["checking"].balance += amount
            self.display_user_balance()
            other_user.display_user_balance()
        else:
            print("Insufficient funds.  Transaction cancelled.")


print("A")
michael = User("Michael","m@m.m")
michael.display_user_balance()
print("B")
michael.make_deposit(200,"checking").make_deposit(300,"savings").make_deposit(400,"checking").make_withdrawal(50,"checking").display_user_balance()
print("C")
julia = User("Julia","j@j.j")
julia.display_user_balance()
michael.transfer_money(75,julia)
# michael.display_info()
# print("D")
# print(michael.enroll())
# print("E")
# michael.spend_points(500)
# michael.display_info()




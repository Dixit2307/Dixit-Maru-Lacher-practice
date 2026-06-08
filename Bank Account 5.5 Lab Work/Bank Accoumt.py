# Bank Account

from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def deposit (self,amount):
        pass

    @abstractmethod
    def withdraw (self,amount):
        pass

class Account(BankAccount):

    def __init__ (self,account_number,balance=0):
        self.__account_number=account_number
        self.__balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance == amount
            print(f" Deposit {amount}")

        else:
            print(f"Invalide Amount: {amount} ")

    def withdraw (self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw Amount {amount}")

        else:
            print(f"Invalide Amount: {amount}")

    def get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance


class SavingAccount(Account):

    def __init__(self,account_number,balance,interest):
        Account.__init__(self,account_number,balance)
        self.interest_rate=interest

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added", interest)

class CurrentAccount(Account):

    def __init__(self , account_number , balance , overdraft = 20000):

        Account.__init__(self , account_number , balance)
        self.overdraft = overdraft

    def withdraw(self , amount):

        if amount <= self.get_balance() + self.overdraft:
            new_bal = self.get_balance() - amount
            self._set_balance(new_bal)
            print("Withdraw", amount)

        else:
            print("Limit of overdraft")


a =Account("A101")
a.deposit(1000)
a.withdraw(10)
print("Balance", a.get_balance())

print("\n--- Saving Account ---\n")
s = SavingAccount("B101", 100000, 5)
s.add_interest() 
s.deposit(2000)
s.withdraw(1000)
print("Saving Balance", s.get_balance())

print("\n===== Current Account =====\n")

c = CurrentAccount("C101", 200000,0 )
c.withdraw(200001)
print("Current Balance ", c.get_balance())




























































            
        

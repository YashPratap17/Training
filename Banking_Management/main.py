from abc import ABC , abstractmethod

class BankAccount(ABC):
    def __init__(self,name,balance):
        self.name = name 
        self.__balance = balance #encapsulation -> priivate variable

    def deposit(self,amount):
        self.__balance += amount #amount added
        print("₹ ",amount," Sucessfully deposited")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount #withdrawn
            print("₹ ",amount," Sucessfully Deducted")


        else:
            print("Insufficient funds")

    def check_balance(self):
        print("Current balance in your account = ₹ ", self.__balance)


    @abstractmethod
    def account_type(self):
        # Abstract method, Abstraction
        pass
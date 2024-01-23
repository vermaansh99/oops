class Account:
    def __init__(self, name, initial_balance):
        self.__name = name
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__display_balance()}")

    def __display_balance(self):
        print(f"Balance: {self.__balance}")


class ManagerAccount(Account):
    def __init__(self, name, initial_balance):
        super().__init__(name, initial_balance)





my_account = Account("John", 1000)
my_account.deposit(500)
# The following lines will cause errors:
# print(my_account.__balance)      # Trying to access a private attribute
my_account.__display_balance()   # Trying to access a private method

manage_account = ManagerAccount("Sumit",10000)

manage_account.__display_balance()
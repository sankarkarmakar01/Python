class Account:
    def __init__(self, bal):
        self.__balance = bal  # private variable

    def show_balance(self):
        print(f"Balance: {self.__balance}")


account1 = Account(1000)
account1.show_balance()
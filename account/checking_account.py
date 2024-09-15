from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str,  overdraft_limit: float = 500.0):
        super().__init__(account_number, balance, account_type)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if self._balance + self.overdraft_limit >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds!")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if self.balance + self.overdraft_limit >= amount:
            self.withdraw(amount)
            destination.deposit(amount)
        else:
            print("Insufficient funds!")

    def show_balance(self) -> None:
        print(f"Checking Account Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self.account_type

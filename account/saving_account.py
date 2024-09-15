from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, interest_rate : float = 9.0):
        super().__init__(account_number, balance, account_type)
        self.set_interest_rate(interest_rate)

    def set_interest_rate(self, interest_rate: float):
        if isinstance(interest_rate, float):
            self._interest_rate = interest_rate
        else:
            print("Interest rate must be a float.")

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}, new balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if self._balance >= amount:
                
                self._balance -= amount
                print(f"Withdrew {amount}, new balance: {self._balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def transfer(self, destination: 'Account', amount: float) -> None:
        if amount > 0:
            if self._balance >= amount:
                self.withdraw(amount)
                destination.deposit(amount)
                print(f"Transferred {amount} to account {destination._account_number}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Transfer amount must be positive.")

    def show_balance(self) -> None:
        print(f"Account Number: {self._account_number}, Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self._account_type

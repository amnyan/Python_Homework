from account import Account
from checking_account import CheckingAccount
from saving_account import SavingsAccount
from typing import Optional
from datetime import datetime

class Transaction:
    def __init__(self, from_account: 'Account', amount: float, transaction_type: str, to_account: Optional['Account'] = None):
        self.set_from_account(from_account)
        self.set_to_account(to_account)
        self.set_amount(amount)
        self.set_transaction_type(transaction_type)
        self._timestamp = datetime.now()

    def set_from_account(self, from_account: 'Account') -> None:
        self._from_account = from_account

    def set_to_account(self, to_account: Optional['Account']) -> None:
        self._to_account = to_account

    def set_amount(self, amount: float) -> None:
        if amount > 0:
            self._amount = amount
        else:
            print("Amount must be positive.")

    def set_transaction_type(self, transaction_type: str) -> None:
        valid_types = {"Deposit", "Withdraw", "Transfer"}
        if transaction_type in valid_types:
            if transaction_type == "Transfer" and self._to_account is None:
                print("Transfer requires a destination account.")
            if transaction_type != "Transfer" and self._to_account is not None:
                print(f"{transaction_type} should not have a destination account.")
            self._transaction_type = transaction_type
        else:
            print("Invalid transaction type. Must be one of 'Deposit', 'Withdraw', or 'Transfer'.")

    def get_from_account(self) -> 'Account':
        return self._from_account

    def get_to_account(self) -> Optional['Account']:
        return self._to_account

    def get_amount(self) -> float:
        return self._amount

    def get_transaction_type(self) -> str:
        return self._transaction_type

    def get_timestamp(self) -> datetime:
        return self._timestamp

    def log(self) -> None:
        """Logs the transaction details."""
        to_account_str = f" to {self.get_to_account()._account_number}" if self.get_to_account() else ""
        print(f"Transaction: {self.get_transaction_type()} of {self.get_amount()} from Account {self.get_from_account()._account_number}"
              f"{to_account_str} at {self.get_timestamp()}")


if __name__ == "__main__":
    checking_account = CheckingAccount(account_number=12345, balance=5000, account_type="Checking")
    savings_account = SavingsAccount(account_number=67890, balance=10000, interest_rate=0.02, account_type="Savings")


    deposit_transaction = Transaction(from_account=checking_account, amount=2000, transaction_type="Deposit")
    deposit_transaction.log() 

    transfer_transaction = Transaction(from_account=checking_account, to_account=savings_account, amount=1000, transaction_type="Transfer")
    transfer_transaction.log()  

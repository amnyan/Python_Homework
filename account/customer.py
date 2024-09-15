from typing import List
from account import Account
from transaction_manager import TransactionManager
from checking_account import CheckingAccount
from jointAccount import JointAccount
from saving_account import SavingsAccount

class Customer:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.accounts: List[Account] = [] 

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)
        print(f"Account {account._account_number} added to customer {self.name}.")

    def view_accounts(self) -> None:
        if not self.accounts:
            print(f"{self.name} has no accounts.")
        else:
            print(f"Accounts for {self.name}")
            for account in self.accounts:
                account.show_balance()


    def view_transaction_history(self) -> None:
        if not self.accounts:
            print(f"{self.name} has no accounts.")
        else:
            print(f"Transaction history for {self.name}:")
            for account in self.accounts:
                print(account)
                if isinstance(account, TransactionManager):
                    account.show_transaction_history()
                else:
                    print(f"Account {account._account_number} does not support transaction history.")
                    
                    


if __name__ == "__main__":
    from datetime import datetime

checking = CheckingAccount(101, 1000.0, "Checking")
savings = SavingsAccount(102, 5000.0, "Savings", 0.5)
joint = JointAccount(103, 2000.0,"Checking", ["Alice", "Bob"])

customer = Customer("John Doe", "john.doe@example.com")
customer.add_account(checking)
customer.add_account(savings)
customer.add_account(joint)


checking.deposit(500.0)
savings.withdraw(1000.0)
joint.transfer(checking, 300.0)

customer.view_accounts()
# customer.view_transaction_history()

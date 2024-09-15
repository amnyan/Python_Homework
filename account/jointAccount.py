from account import Account
from typing import List


class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, joint_owners: List[str]):
        super().__init__(account_number, balance, account_type)
        self.joint_owners = joint_owners

    def add_owner(self, customer_name: str) -> None:
        if isinstance(customer_name, str):
            if customer_name not in self.joint_owners:
                self.joint_owners.append(customer_name)
                print(f"{customer_name} has been added as a joint owner.")
            else:
                print(f"{customer_name} is already an owner.")
        else:
            print("Customer name must be a string.")

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}, new balance: {self._balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

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
        owners = ", ".join(self.joint_owners)
        print(f"Account Number: {self._account_number}, Owners: {owners}, Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self._account_type
    

if __name__ == "__main__":        
    joint_account = JointAccount(account_number=67890, balance=5000,account_type="jointAccount" ,joint_owners=["Alice", "Bob"])
    joint_account.deposit(1000) 
    joint_account.withdraw(2000) 
    joint_account.add_owner("Hasmik") 

    joint_account.show_balance()



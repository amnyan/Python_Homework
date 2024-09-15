import abc


class Account(abc.ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self.set_acc_number(account_number)
        self.set_balance(balance)
        self.set_account_type(account_type)


    def set_acc_number(self, number):
        if isinstance(number, int):
            self._account_number = number
        else :
            self._account_number = None
    
    def set_balance(self, balance):
        if isinstance(balance, float):
            self._balance = balance
        else :
            self._balance = 0
            
    def set_account_type(self, type):
        if isinstance(type, str):
            self._account_type = type
        else :
            self._account_type = None
            
    
    @abc.abstractmethod
    def deposit(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        ...

    @abc.abstractmethod
    def show_balance(self) -> None:
        ...

    @abc.abstractmethod
    def get_account_type(self) -> str:
        ...
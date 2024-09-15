import abc

class TransactionManager(abc.ABC):
    @abc.abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
       ...

    @abc.abstractmethod
    def show_transaction_history(self) -> None:
        ...

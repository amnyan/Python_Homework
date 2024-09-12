#Design a class Book with private attributes title, author, and price. Create methods to set and get the values of these attributes. Ensure that the price cannot be set below a certain value (e.g., 10).
class Book:
    def __init__(self, title: str, author: str, price: float) -> None:
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)


    def set_title(self, title: str) -> None:
        if isinstance(title, str) and len(title) > 0:
            self.__title = title
        else:
            self.__title = None


    def set_author(self, author: str) -> None:
        if isinstance(author, str) and len(author) > 0:
            self.__author = author
        else:
            self.__author = None


    def set_price(self, price: float) -> None:
        if isinstance(price, (int, float)) and price >= 10:
            self.__price = price
        else:
            print("Price cannot be less than 10.")
            self.__price = None


    def get_title(self) -> str:
        return self.__title


    def get_author(self) -> str:
        return self.__author


    def get_price(self) -> float:
        return self.__price


    def display(self) -> None:
        print(f"Title: {self.get_title()} | Author: {self.get_author()} | Price: ${self.get_price()}")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 20)
book1.display()


book2 = Book("1984", "George Orwell", 8)
book2.display()

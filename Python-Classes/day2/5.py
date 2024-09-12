# Design a class Product with private attributes product_id, product_name, and quantity_in_stock. Implement methods to set and get the values of these attributes and to adjust the quantity_in_stock (e.g., adding stock or reducing stock).

class Product:
    def __init__(self, product_id: int, product_name: str, quantity_in_stock: int) -> None:
        self.set_product_id(product_id)
        self.set_product_name(product_name)
        self.set_quantity_in_stock(quantity_in_stock)

    def set_product_id(self, product_id: int) -> None:
        if isinstance(product_id, int) and product_id > 0:
            self.__product_id = product_id
        else:
            self.__product_id = None

    def set_product_name(self, product_name: str) -> None:
        if isinstance(product_name, str) and len(product_name) > 0:
            self.__product_name = product_name
        else:
            self.__product_name = None

    def set_quantity_in_stock(self, quantity_in_stock: int) -> None:
        if isinstance(quantity_in_stock, int) and quantity_in_stock >= 0:
            self.__quantity_in_stock = quantity_in_stock
        else:
            self.__quantity_in_stock = None

    def get_product_id(self) -> int:
        return self.__product_id

    def get_product_name(self) -> str:
        return self.__product_name

    def get_quantity_in_stock(self) -> int:
        return self.__quantity_in_stock

    def adjust_stock(self, amount: int) -> None:
        if isinstance(amount, int):
            new_quantity = self.__quantity_in_stock + amount
            if new_quantity >= 0:
                self.__quantity_in_stock = new_quantity
            else:
                print("Cannot reduce stock below zero.")
        else:
            print("Invalid amount. It must be an integer.")

    def display(self) -> None:
        print(f"Product ID: {self.get_product_id()} | Name: {self.get_product_name()} | Quantity in Stock: {self.get_quantity_in_stock()}")

# Example usage
product = Product(101, "Laptop", 50)
product.display()

product.adjust_stock(20)
product.display()

product.adjust_stock(-30)
product.display()

product.adjust_stock(-50)
product.display()

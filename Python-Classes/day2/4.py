class ShoppingCart:
    def __init__(self) -> None:
        self.__items = [] 

  
    def add_item(self, name: str, price: float) -> None:
        if isinstance(name, str) and isinstance(price, (int, float)) and price > 0:
            self.__items.append({"name": name, "price": price})
            print(f"Added {name} to the cart at ${price:.2f}")
        else:
            print("Invalid item or price. Ensure the price is positive.")

   
    def remove_item(self, name: str) -> None:
        for item in self.__items:
            if item["name"] == name:
                self.__items.remove(item)
                print(f"Removed {name} from the cart.")
                return
        print(f"Item {name} not found in the cart.")

    def total_items(self) -> int:
        return len(self.__items)

   
    def display_cart(self) -> None:
        if not self.__items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            total_price = 0
            for item in self.__items:
                print(f"{item['name']} - ${item['price']:.2f}")
                total_price += item['price']
            print(f"Total items: {self.total_items()} | Total price: ${total_price:.2f}")


cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 49.99)
cart.display_cart()

cart.remove_item("Mouse")
cart.display_cart()

cart.remove_item("Keyboard")

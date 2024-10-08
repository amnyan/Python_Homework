class MenuItem:
    __slots__ = ("__price","__name","__ingredients")
    
    
    def __init__(self, name:str, price:float, ingredients:list):
        self.name = name
        self.price=  price
        self.ingredients = ingredients
        
        
    @property
    def name(self)->str:
        return self.__name
    
    
    @name.setter
    def name(self, value:str)->None:
        if isinstance(value,str) and value != "":
            self.__name = value
        else:
            raise ValueError("Name must be String and NOT Empyt")
            
    @property
    def price(self)->str:
        return self.__price
    
    
    @price.setter
    def price(self, value:float)->None:
        if not (isinstance(value,(float,int)) and value > 0):
            raise ValueError("Price must be Float/Int and grather than Zero")
        self.__price = value
        
        
    @property
    def ingredients(self)->list:
        return self.__ingredients
    
    
    @ingredients.setter
    def ingredients(self, value:list)->None:
        if not (isinstance(value,list) and value != []):
            raise ValueError("ingredients must be List and NOT Empyt")
        self.__ingredients = value
        
        
        
    def __str__(self)->str:
        return f'''MenuItem object 
                (name : {self.name},
                (price : {self.price}),
                (ingredients : {self.ingredients})`)
                '''
    
class Appetizer(MenuItem):
    __slots__ = ("__serving_size")
    serving_types = ["Small", "Medium","Large"]
    
    def __init__(self,name:str, price:float, ingredients:list, serving_size:str):
        super().__init__(name,price, ingredients)
        self.serving_size = serving_size
        
        
    @property
    def serving_size(self)->str:
        return self.__serving_size
    
    
    @serving_size.setter
    def serving_size(self, value:str)-> None:
        if value in self.serving_types:
            self.__serving_size = value
        else:
            raise ValueError("Serving size must be 'Small', 'Medium', or 'Large'")
    
    
class Entree(MenuItem):
    __slots__ = ("__cooking_method")
    cooking_method_type = ["Grilled", "Fried", "Baked","Roasted"]
    
    def __init__(self,name:str, price:float, ingredients:list, cooking_method:str):
        super().__init__(name,price, ingredients)
        self.cooking_method = cooking_method
        
        
    @property
    def cooking_method(self)->str:
        return self.__cooking_method
    
    
    @cooking_method.setter
    def cooking_method(self, value:str)-> None:
        if value in self.cooking_method_type:
            self.__cooking_method = value
        else:
            raise ValueError("cooking_method must be 'Grilled', 'Fried', 'Baked','Roasted'")
    
class Dessert(MenuItem):
    
    __slots__ = ("__sweetness_level")
    sweetness_type = ["Very Sweet", "Moderate", "Lightly Sweet"]
    
    def __init__(self,name:str, price:float, ingredients:list, sweetness_level:str):
        super().__init__(name,price, ingredients)
        self.sweetness_level = sweetness_level
        
        
    @property
    def sweetness_level(self)->str:
        return self.__sweetness_level
    
    
    @sweetness_level.setter
    def sweetness_level(self, value:str)-> None:
        if value in self.sweetness_type:
            self.__sweetness_level = value
        else:
            raise ValueError("sweetness_level must be 'Very Sweet', 'Moderate', 'Lightly Sweet'")
        
        
        
class Customer:
    __slots__ = ("__name", "__contact_info","__order_history")
    
    def __init__(self, name:str, contact_info:dict):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []
        
        
    @property
    def name(self)->str:
        return self.__name
    
    
    @name.setter
    def name(self, value):
        if  isinstance(value, str) and value != "":
            self.__name =value
        else:
            raise ValueError("name must be string and not empty")
        
    @property
    def contact_info(self)->str:
        return self.__contact_info
    
    
    @contact_info.setter
    def contact_info(self, value):
        if  isinstance(value, dict) :
            self.__contact_info =value
        else:
            raise ValueError("Contact info must be in this format (+374 xx xxx-xxx)")
        
    @property
    def order_history(self)->str:
        return self.__order_history
    
    @order_history.setter
    def order_history(self, value):
        self.__order_history = value
    
        
    def place_order(self, order):
        self.order_history.append(order)
        
    def view_order_history(self):
        return self.order_history
    
    
    def leave_review(self, order, rating, comments):
        review = Review(self.name, order, rating, comments)
        
        
from abc import ABC, abstractmethod

class Order(ABC):
    __slots__ = ['customer', 'menu_items', 'total_price']
    
    def __init__(self, customer):
        self.customer = customer 
        self.menu_items = [] 
        self.total_price = 0.0  
    
    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item) 
        self.calculate_total_price() 
    
    def remove_menu_item(self, menu_item):
        self.menu_items.remove(menu_item) 
        self.calculate_total_price() 

    def calculate_total_price(self):
        self.total_price = sum(item.price for item in self.menu_items) 

    @abstractmethod
    def finalize_order(self):
        ...
        
class DineInOrder(Order):
    __slots__ = ('table_number')

    def __init__(self, customer, table_number):
        super().__init__(customer) 
        self.table_number = table_number 

    def finalize_order(self):
        # Logic to finalize a dine-in order
        print(f"Order finalized for table {self.table_number}")
        
        
class TakeawayOrder(Order):
    __slots__ = ('pickup_time')

    def __init__(self, customer, pickup_time):
        super().__init__(customer)  
        self.pickup_time = pickup_time  

    def finalize_order(self):
        # Logic to finalize a takeaway order
        print(f"Order ready for pickup at {self.pickup_time}")


class DeliveryOrder(Order):
    __slots__ = ('delivery_address')

    def __init__(self, customer, delivery_address):
        super().__init__(customer)  
        self.delivery_address = delivery_address  

    def finalize_order(self):
        # Logic to finalize a delivery order
        print(f"Order will be delivered to {self.delivery_address}")


class Order(ABC):
    __slots__ = ('customer', 'menu_items', 'total_price')

    def __init__(self, customer):
        self.customer = customer  
        self.menu_items = []  
        self.total_price = 0.0

    def add_menu_item(self, menu_item):
        
        self.menu_items.append(menu_item)
        self.calculate_total_price()

    def remove_menu_item(self, menu_item):
       
        self.menu_items.remove(menu_item)
        self.calculate_total_price()

    def calculate_total_price(self):
        
        self.total_price = sum(item.price for item in self.menu_items)

    @abstractmethod
    def finalize_order(self):
       ...
       
class DineInOrder(Order):
    __slots__ = ['table_number']

    def __init__(self, customer, table_number):
        super().__init__(customer)
        self.table_number = table_number

    def finalize_order(self):
        print(f"Order finalized for table {self.table_number}")
        
        
class TakeawayOrder(Order):
    __slots__ = ['pickup_time']

    def __init__(self, customer, pickup_time):
        super().__init__(customer)
        self.pickup_time = pickup_time 

    def finalize_order(self):
        print(f"Order ready for pickup at {self.pickup_time}")
        
        
        
class DeliveryOrder(Order):
    __slots__ = ['delivery_address']

    def __init__(self, customer, delivery_address):
        super().__init__(customer)
        self.delivery_address = delivery_address 

    def finalize_order(self):
        print(f"Order will be delivered to {self.delivery_address}")



class Review:
    __slots__ = ['customer_name', 'order', 'rating', 'comments']  # Using __slots__ for memory optimization

    def __init__(self, customer_name, order, rating, comments):
        self.customer_name = customer_name  # Name of the customer leaving the review
        self.order = order  # The order being reviewed
        self.rating = rating  # Rating given by the customer
        self.comments = comments  # Additional comments from the customer

    def __str__(self):
        """Return a string representation of the review."""
        return (f"Review by {self.customer_name}:\n"
                f"Rating: {self.rating}\n"
                f"Comments: {self.comments}")




import unittest

class TestRestaurantManagement(unittest.TestCase):

    def test_menu_item_initialization(self):
        item = MenuItem("Salad", 10.0, ["Lettuce", "Tomato"])
        self.assertEqual(item.name, "Salad")
        self.assertEqual(item.price, 10.0)
        self.assertEqual(item.ingredients, ["Lettuce", "Tomato"])

    def test_appetizer_initialization(self):
        appetizer = Appetizer("Wings", 5.0, ["Chicken", "Sauce"], "Medium")
        self.assertEqual(appetizer.name, "Wings")
        self.assertEqual(appetizer.serving_size, "Medium")

    def test_entree_initialization(self):
        entree = Entree("Steak", 20.0, ["Beef"], "Grilled")
        self.assertEqual(entree.name, "Steak")
        self.assertEqual(entree.cooking_method, "Grilled")

    def test_dessert_initialization(self):
        dessert = Dessert("Cake", 7.0, ["Flour", "Sugar"], "Very Sweet")
        self.assertEqual(dessert.name, "Cake")
        self.assertEqual(dessert.sweetness_level, "Very Sweet")

    def test_customer_initialization(self):
        customer = Customer("John Doe", {"phone": "+374 77 123-456"})
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.contact_info, {"phone": "+374 77 123-456"})

    def test_place_order(self):
        customer = Customer("Jane Doe", {"phone": "+374 77 123-456"})
        order = DineInOrder(customer, 5)
        customer.place_order(order)
        self.assertIn(order, customer.order_history)

    def test_order_total_price(self):
        item1 = MenuItem("Pasta", 12.0, ["Noodles", "Sauce"])
        item2 = MenuItem("Salad", 8.0, ["Lettuce", "Tomato"])
        order = DineInOrder(Customer("Customer", {"phone": "+374 77 123-456"}), 5)
        order.add_menu_item(item1)
        order.add_menu_item(item2)
        self.assertEqual(order.total_price, 20.0)

    def test_review(self):
        customer = Customer("John Doe", {"phone": "+374 77 123-456"})
        order = DineInOrder(customer, 5)
        review = Review(customer.name, order, 5, "Great food!")
        self.assertEqual(review.customer_name, "John Doe")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comments, "Great food!")


if __name__ == "__main__":
    unittest.main()

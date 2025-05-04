
from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    @abstractmethod
    def getPrice(self):
        pass
    
class Candy(DessertItem):
    # candy by kgs -- gms and price per kg
    def __init__(self, name, qty):
        super().__init__(name)
        self.qty = qty
        self.price = 300 * (qty/1000)
        
    def getPrice(self):
        return self.price

class Cookie(DessertItem):
    # cookies by dozen -- number(units) price per dozen
    def __init__(self, name, qty):
        super().__init__(name)
        self.qty = qty
        self.price = 120 * (qty/12)
        
    def getPrice(self):
        return self.price

class IceCream(DessertItem):
    # cost in rupees
    def __init__(self, name, qty):
        super().__init__(name)
        self.qty = qty
        self.price = 50 * qty
        
    def getPrice(self):
        return self.price

class Sundae(IceCream):
    # cost in ruppes + toppings
    def __init__(self, name, qty):
        super().__init__(name, qty)
        self.qty = qty
        self.toppings_price = 10
        self.price = super().getPrice() + self.toppings_price
        
    def getPrice(self):
        return self.price
                
class Checkout:
    # Enter dessertitem in cashRegister (this can be collection)
    # clear cash register
    # get number of items
    # get total cost of items
    # get String representing all items in cart and their total (invoice)
    
    dessert_items_list = []
    total_price = 0
    checkout_flag = True
    
    while checkout_flag:        
        dessert_item = input("Select Dessert Item: \n1. Candy \n2. Cookie \n3. Ice Cream \n4. Sundae\n5. Checkout\n")
        
        if not dessert_item == "5":
            dessert_item_qty = int(input("Enter Quantity: "))
                
        if dessert_item == "1":
            candy = Candy("Candy", dessert_item_qty)
            dessert_items_list.append(candy)
            print(f"Candy Added: {candy.getName()}")
        elif dessert_item == "2":
            cookie = Cookie("Cookie", dessert_item_qty)
            dessert_items_list.append(cookie)
            print(f"Cookie Added: {cookie.getName()}")
        elif dessert_item == "3":
            icecream = IceCream("Ice Cream", dessert_item_qty)
            dessert_items_list.append(icecream)
            print(f"Ice Cream Added: {icecream.getName()}")
        elif dessert_item == "4":
            sundae = Sundae("Sundae", dessert_item_qty)
            dessert_items_list.append(sundae)
            print(f"Sundae Added: {sundae.getName()}")
        elif dessert_item == "5":
            checkout_flag = False
            print("Checkout")
        else:
            print("Invalid Input, Please try again")
        
    
    
    # print("Invoice")
    # for item in dessert_items_list:
    #     print(f"{item.getName()} : {item.getPrice()}")
    # total_price = sum([item.getPrice() for item in dessert_items_list])
    # print(f"Total Price: {total_price}")

    # Do Later
    # Exception - Cart Empty
    # Exception - Something went wrong
        
    if not dessert_items_list:
        raise Exception("Cart is empty. Please add items before checkout.")
    else:
        try:
            print("Invoice")
            for item in dessert_items_list:
                print(f"{item.getName()} : {item.getPrice()}")
            total_price = sum([item.getPrice() for item in dessert_items_list])
            print(f"Total Price: {total_price}")
        except Exception as e:
            print(f"Something went wrong: {e}")
    
    
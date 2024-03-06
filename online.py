import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from enum import Enum
from datetime import datetime


# Define Enums and Constants
class OrderStatus(Enum):
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class ShipmentStatus(Enum):
    PENDING, SHIPPED, DELIVERED, ON_HOLD = 1, 2, 3, 4

class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Define classes
class Account:
    def __init__(self, user_name, password, name, email, phone, shipping_address, status=AccountStatus):
        self.__user_name = user_name
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__shipping_address = shipping_address
        self.__status = status.ACTIVE
        self.__credit_cards = []
        self.__bank_accounts = []

    def add_product(self, product):
        # Logic to add a product
        pass

    def add_product_review(self, product, review):
        # Logic to add a review for a product
        pass

    def reset_password(self):
        # Logic to reset password
        pass

class Customer:
    def __init__(self, cart, order):
        self.__cart = cart
        self.__order = order

    def get_shopping_cart(self):
        return self.__cart

    def add_item_to_cart(self, item):
        # Logic to add an item to the cart
        self.__cart.add_item(item)

    def remove_item_from_cart(self, item):
        # Logic to remove an item from the cart
        self.__cart.remove_item(item)

class Guest(Customer):
    def register_account(self):
        # Logic to register an account
        pass

class Member(Customer):
    def __init__(self, account):
        self.__account = account

    def place_order(self, order):
        # Logic to place an order
        order.make_payment()
        order.send_for_shipment()

class ProductCategory:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

class ProductReview:
    def __init__(self, rating, review, reviewer):
        self.__rating = rating
        self.__review = review
        self.__reviewer = reviewer

class Product:
    def __init__(self, id, name, description, price, category, seller_account, available_item_count):
        self.__product_id = id
        self.__name = name
        self.__description = description
        self.__price = price  
        self.__category = category
        self.__available_item_count = available_item_count
        self.__seller = seller_account

    def get_name(self):
        return self.__name

    def get_available_count(self):
        return self.__available_item_count

    def get_price(self):  # Define get_price method to access the price attribute
        return self.__price

    def update_price(self, new_price):
        # Logic to update the price of a product
        self.__price = new_price


class Item:
    def __init__(self, product, quantity, price):
        self.__product = product
        self.__quantity = quantity
        self.__price = price

    def update_quantity(self, quantity):
        # Logic to update the quantity of an item
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        # Logic to add an item to the shopping cart
        self.__items.append(item)

    def remove_item(self, item):
        # Logic to remove an item from the shopping cart
        self.__items.remove(item)

    def update_item_quantity(self, item, quantity):
        # Logic to update the quantity of an item in the shopping cart
        for cart_item in self.__items:
            if cart_item == item:
                cart_item.update_quantity(quantity)
                break

    def checkout(self):
        # Logic to checkout the items in the shopping cart
        pass

    def get_items(self):
        return self.__items

class OrderLog:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = order_number
        self.__order_date = datetime.today().date()
        self.__status = status

class Order:
    def __init__(self, order_number, status=OrderStatus.PENDING):
        self.__order_number = order_number
        self.__status = status
        self.__order_date = datetime.today().date()
        self.__order_log = []

    def send_for_shipment(self):
        # Logic to send the order for shipment
        pass

    def make_payment(self):
        # Logic to make payment for the order
        pass

    def add_order_log(self, order_log):
        # Logic to add an order log
        pass

class ShipmentLog:
    def __init__(self, shipment_number, status=ShipmentStatus.PENDING):
        self.__shipment_number = shipment_number
        self.__status = status
        self.__order_date = datetime.today().date()

class Shipment:
    def __init__(self, shipment_number, shipment_method):
        self.__shipment_number = shipment_number
        self.__shipment_date = datetime.date.today()
        self.__estimated_arrival = datetime.date.today()
        self.__shipment_method = shipment_method
        self.__shipment_logs = []

    def add_shipment_log(self, shipment_log):
        # Logic to add a shipment log
        pass

class Notification:
    def __init__(self, id, content):
        self.__notification_id = id
        self.__order_date = datetime.today().date()
        self.__content = content

    def send_notification(self, account):
        # Logic to send a notification
        pass

class Search:
    def __init__(self, catalog):
        self.__catalog = catalog

    def search_products_by_name(self, name):
        # Logic to search products by name
        products = self.__catalog.search_products_by_name(name)
        available_products = [product for product in products if product.get_available_count() > 0]
        return available_products

    def search_products_by_category(self, category):
        # Logic to search products by category
        products = self.__catalog.search_products_by_category(category)
        available_products = [product for product in products if product.get_available_count() > 0]
        return available_products

class Catalog:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        self.__products[product.get_name()] = product

    def search_products_by_name(self, name):
        if name == "":
            return list(self.__products.values())  
        elif name in self.__products:
            return [self.__products[name]]
        else:
            return []


    def search_products_by_category(self, category):
        products = []
        for product in self.__products.values():
            if product.get_category() == category:
                products.append(product)
        return products

class OnlineShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Shopping System")
        self.root.geometry("800x600")

        # Create catalog
        self.catalog = Catalog()

        # Add some sample products
        self.catalog.add_product(Product(1, "Laptop", "High performance laptop", 1000, "Electronics", None, 5))
        self.catalog.add_product(Product(2, "Smartphone", "Latest smartphone model", 500, "Electronics", None, 10))
        self.catalog.add_product(Product(3, "Book", "Bestseller book", 20, "Books", None, 15))

        self.initialize_components()

    def initialize_components(self):
        # Create and place GUI components here
        label = tk.Label(self.root, text="Welcome to Online Shopping System", font=("Arial", 18))
        label.pack(pady=20)

        button_search = tk.Button(self.root, text="Search Products", command=self.search_products)
        button_search.pack(pady=10)

        button_add_product = tk.Button(self.root, text="Add Product", command=self.add_product)
        button_add_product.pack(pady=10)

        button_add_review = tk.Button(self.root, text="Add Review", command=self.add_review)
        button_add_review.pack(pady=10)

        button_place_order = tk.Button(self.root, text="Place Order", command=self.place_order)
        button_place_order.pack(pady=10)

    def search_products(self):
        # Implement search functionality
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Products")

        # Add search functionality here
        search_label = tk.Label(search_window, text="Search Products:")
        search_label.pack()

        search_entry = tk.Entry(search_window)
        search_entry.pack()

        search_button = tk.Button(search_window, text="Search", command=lambda: self.search_action(search_entry.get()))
        search_button.pack()

    def add_product(self):
        # Implement functionality to add a product
        add_product_window = tk.Toplevel(self.root)
        add_product_window.title("Add Product")

        # Add product functionality here
        product_name_label = tk.Label(add_product_window, text="Product Name:")
        product_name_label.pack()

        product_name_entry = tk.Entry(add_product_window)
        product_name_entry.pack()

        product_desc_label = tk.Label(add_product_window, text="Product Description:")
        product_desc_label.pack()

        product_desc_entry = tk.Entry(add_product_window)
        product_desc_entry.pack()

        product_price_label = tk.Label(add_product_window, text="Product Price:")
        product_price_label.pack()

        product_price_entry = tk.Entry(add_product_window)
        product_price_entry.pack()

        add_button = tk.Button(add_product_window, text="Add Product", command=lambda: self.add_product_action(add_product_window, product_name_entry.get(), product_desc_entry.get(), float(product_price_entry.get())))
        add_button.pack()

    def add_review(self):
        # Implement functionality to add a review
        add_review_window = tk.Toplevel(self.root)
        add_review_window.title("Add Review")

        # Add review functionality here
        available_product_names = [product.get_name() for product in self.catalog.search_products_by_name("")]
        product_combo = tk.ttk.Combobox(add_review_window, values=available_product_names)
        product_combo.pack()

        review_label = tk.Label(add_review_window, text="Review:")
        review_label.pack()

        review_entry = tk.Entry(add_review_window)
        review_entry.pack()

        add_button = tk.Button(add_review_window, text="Add Review", command=lambda: self.add_review_action(add_review_window, product_combo.get(), review_entry.get()))
        add_button.pack()

    def place_order(self):
        # Implement functionality to place an order
        place_order_window = tk.Toplevel(self.root)
        place_order_window.title("Place Order")

        # Add place order functionality here
        available_product_names = [product.get_name() for product in self.catalog.search_products_by_name("")]
        product_combo = tk.ttk.Combobox(place_order_window, values=available_product_names)
        product_combo.pack()

        order_button = tk.Button(place_order_window, text="Place Order", command=lambda: self.place_order_action(place_order_window, product_combo.get()))
        order_button.pack()

    def search_action(self, search_query):
        # Perform search action here
        available_products = self.catalog.search_products_by_name(search_query)
        if available_products:
            messagebox.showinfo("Search Result", f"Available products: {[product.get_name() for product in available_products]}")


        else:
            messagebox.showinfo("Search Result", "No products found.")
     
     
        

    def add_product_action(self, window, product_name, product_description, product_price):
        # Perform add product action here
        self.catalog.add_product(Product(len(self.catalog.search_products_by_name("")), product_name, product_description, product_price, "", None, 0))
        messagebox.showinfo("Add Product Action", f"Product '{product_name}' added successfully.")
        window.destroy()

    def add_review_action(self, window, product_name, review_text):
        # Perform add review action here
        product = self.catalog.search_products_by_name(product_name)[0]
        account = Account("username", "password", "John Doe", "john@example.com", "1234567890", None)
        account.add_product_review(product, review_text)
        messagebox.showinfo("Add Review Action", f"Review added for product '{product_name}'.")
        window.destroy()

    def place_order_action(self, window, product_name):
        # Perform place order action here
        product = self.catalog.search_products_by_name(product_name)[0]
        account = Account("username", "password", "John Doe", "john@example.com", "1234567890", None)
        cart = ShoppingCart()
        cart.add_item(Item(product, 1, product.get_price()))
        order = Order(1)
        order.add_order_log(OrderLog(1))
        member = Member(account)
        member.place_order(order)
        # Show a message confirming the order placement
        messagebox.showinfo("Order Placed", f"Order placed successfully for '{product_name}'.")
        window.destroy()

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineShoppingApp(root)
    root.mainloop()



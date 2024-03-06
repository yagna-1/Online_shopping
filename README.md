# This code implements an online shopping system using object-oriented principles in Python with the Tkinter library for the GUI. Let's break down the functionality and discuss how object-oriented design (OOD) principles were used:

# Classes and Objects:

# The code defines several classes such as Account, Customer, Product, Order, ShoppingCart, etc., to represent entities in the system.
# Objects of these classes are created to model real-world entities. For example, an Account object represents a user account, a Product object represents a product available for purchase, and so on.
# Encapsulation:

# Encapsulation is demonstrated by using private attributes and methods in classes, which can only be accessed or modified through public methods. For example, attributes like __user_name, __password, __name, etc., in the Account class are encapsulated to prevent direct access from outside the class.
# Inheritance:

# The code uses inheritance to create specialized classes based on more general ones. For example, the Customer class inherits from the Account class, and Guest and Member are further specialized subclasses of Customer.
# Polymorphism:

# Polymorphism is achieved through method overriding. Subclasses override methods from their parent classes to provide their own implementation. For instance, Member class overrides the place_order method inherited from the Customer class to include additional functionality specific to members.
# Composition:

# Composition is demonstrated by creating objects of one class within another class. For example, the ShoppingCart class contains a list of Item objects, and the Order class contains a list of OrderLog objects.
# Enums and Constants:

# Enumerations (OrderStatus, AccountStatus, ShipmentStatus, PaymentStatus) and constants are used to represent predefined states or values in the system, enhancing code readability and maintainability.
# Dependency Injection:

# Dependency Injection is used implicitly throughout the code. For example, when an Order object is created, it requires an OrderLog object to be passed in. This allows for better decoupling and testability of the code.
# From a low-level system point of view:

# Each class represents an entity or a component in the system, such as accounts, products, orders, etc.
# Attributes and methods within each class encapsulate the behavior and data associated with that entity or component.
# The interactions between different classes simulate the flow of actions and processes in an online shopping system, such as adding products, placing orders, etc.
# Enums and constants define and manage the various states and statuses that these entities can have, ensuring consistency and clarity in the code.

# Encapsulation:

# Encapsulation refers to the bundling of data and methods that operate on the data within a single unit, such as a class. It hides the internal state of an object and only exposes the necessary functionalities. In the code:
# All class attributes are defined as private variables using double underscores (__), such as self.__user_name, self.__password, etc., in classes like Account, Product, Item, etc. This encapsulates the internal state of the objects and restricts direct access to them from outside the class.
# Methods like add_product, add_product_review, reset_password, get_name, update_quantity, etc., are used to manipulate the internal state of objects, encapsulating the behavior within the respective classes.
# Inheritance:

# Inheritance allows a class (subclass) to inherit attributes and methods from another class (superclass). It promotes code reusability and establishes a hierarchical relationship between classes. In the code:
# Class Customer inherits from class Object, implicitly.
# Classes Guest and Member inherit from class Customer, indicating that they share common behavior and attributes with the Customer class. They extend the functionality of the Customer class with additional methods like register_account and place_order, respectively.
# Polymorphism:

# Polymorphism allows objects of different classes to be treated as objects of a common superclass, enabling the same interface to be used for different types of objects. It promotes flexibility and modularity in the code. In the code:
# The place_order method in the Member class exhibits polymorphic behavior by accepting an Order object as an argument. It demonstrates the ability to process orders differently based on the specific type of customer (member).
# Abstraction:

# Abstraction involves hiding the complex implementation details and showing only the essential features of an object. It focuses on what an object does rather than how it does it. In the code:
# Classes like Account, Customer, Product, Item, etc., encapsulate the internal details and provide a clear interface for interacting with the objects. External users can utilize the methods exposed by these classes without needing to understand their internal implementation.
# The search_action, add_product_action, add_review_action, and place_order_action methods in the OnlineShoppingApp class abstract away the implementation details of searching products, adding products/reviews, and placing orders, providing a simplified interface for users interacting with the GUI.

#Account Class:

# This class represents a user account in the online shopping system.
# Attributes: user_name, password, name, email, phone, shipping_address, status, credit_cards, bank_accounts.
# OOD Principles:
# Encapsulation: Attributes are encapsulated (private) to control access to them. Methods like reset_password, add_product, add_product_review provide controlled access to modify account data.
# Composition: credit_cards and bank_accounts are composed within the Account class, representing a relationship where an account can have multiple credit cards and bank accounts.
# Customer Class:

# Represents a customer in the system.
# Attributes: cart, order.
# OOD Principles:
# Inheritance: Inherits common functionalities from the Account class, as all customers are also accounts.
# Composition: cart and order objects are composed within the Customer class to manage a customer's shopping cart and orders.
# Guest Class:

# Represents a guest user who is not registered.
# Methods: register_account.
# OOD Principles:
# Inheritance: Inherits from the Customer class to utilize its functionalities.
# Member Class:

# Represents a registered member in the system.
# Attributes: account.
# Methods: place_order.
# OOD Principles:
# Composition: Contains an Account object, demonstrating composition.
# Polymorphism: Overrides the place_order method from the Customer class to add member-specific functionalities.
# ProductCategory Class:

# Represents a category of products.
# Attributes: name, description.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, providing controlled access to category data.
# ProductReview Class:

# Represents a review of a product.
# Attributes: rating, review, reviewer.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods can be used to interact with review data.
# Product Class:

# Represents a product available for purchase.
# Attributes: product_id, name, description, price, category, seller, available_item_count.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to product data.
# Composition: Contains a Seller object, demonstrating composition.
# Item Class:

# Represents an item in the shopping cart.
# Attributes: product, quantity, price.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to item data.
# ShoppingCart Class:

# Represents a shopping cart for a customer.
# Attributes: items.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to cart data.
# Composition: Contains a list of Item objects, demonstrating composition.
# OrderLog Class:

# Represents a log entry for an order.
# Attributes: order_number, order_date, status.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to log data.
# Order Class:

# Represents an order placed by a customer.
# Attributes: order_number, status, order_date, order_log.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to order data.
# Composition: Contains a list of OrderLog objects, demonstrating composition.
# ShipmentLog Class:

# Represents a log entry for a shipment.
# Attributes: shipment_number, status, order_date.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to log data.
# Shipment Class:

# Represents a shipment of an order.
# Attributes: shipment_number, shipment_date, estimated_arrival, shipment_method, shipment_logs.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to shipment data.
# Composition: Contains a list of ShipmentLog objects, demonstrating composition.
# Notification Class:

# Represents a notification sent to a user.
# Attributes: notification_id, order_date, content.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to notification data.
# Search Class:

# Represents a search functionality for products.
# Attributes: catalog.
# Methods: search_products_by_name, search_products_by_category.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to search functionality.
# Catalog Class:

# Represents a catalog of products available in the system.
# Attributes: products.
# Methods: add_product, search_products_by_name, search_products_by_category.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to catalog data.
# OnlineShoppingApp Class:

# Represents the main application interface for the online shopping system.
# Attributes: root, catalog.
# Methods: initialize_components, search_products, add_product, add_review, place_order, and related action methods.
# OOD Principles:
# Encapsulation: Attributes are encapsulated, and methods provide controlled access to app functionalities.
# Composition: Contains a Catalog object, demonstrating composition.

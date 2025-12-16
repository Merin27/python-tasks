# Shopping Cart

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def total_price(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        for item in self.cart:
            if item.name == product.name:
                item.quantity += product.quantity
                return
        self.cart.append(product)

    def remove_product(self, product_name):
        self.cart = [item for item in self.cart if item.name != product_name]

    def calculate_total(self):
        return sum(item.total_price() for item in self.cart)

    def show_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            for item in self.cart:
                print(f"{item.name}: {item.quantity} pcs - ₹{item.total_price():.2f}")
            print(f"Total Price: ₹{self.calculate_total():.2f}")

cart = ShoppingCart()
cart.add_product(Product("Dresses", 999, 3))
cart.add_product(Product("Bags", 799, 2))
cart.add_product(Product("Shoes", 849, 1))
cart.show_cart()

cart.add_product(Product("Dresses", 999, 2))
print("\nAfter adding more Dresses:")
cart.show_cart()

cart.remove_product("Shoes")
print("\nAfter removing Shoes:")
cart.show_cart()

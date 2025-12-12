class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, id={self.product_id})"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer(name={self.name}, email={self.email})"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.product_id != product_id]

    def total_price(self):
        return sum(p.price for p in self.products)


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def order_confirmation(self):
        product_list = ", ".join(p.name for p in self.products)
        total = sum(p.price for p in self.products)
        return (
            f"Bestellbestätigung für {self.customer.name} (Email: {self.customer.email}):\n"
            f"Produkte: {product_list}\n"
            f"Gesamtpreis: {total} €"
        )


# --- Test-Durchlauf ---
if __name__ == "__main__":
    # Produkte erstellen
    p1 = Product("Laptop", 1200, 1)
    p2 = Product("Maus", 25, 2)
    p3 = Product("Tastatur", 45, 3)

    # Kunde erstellen
    customer = Customer("Anna Müller", "anna.mueller@example.com")

    # Einkaufswagen verwenden
    cart = ShoppingCart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    cart.remove_product(2)  # Maus entfernen

    print("Warenkorb-Produkte:", cart.products)
    print("Gesamtpreis:", cart.total_price(), "€")

    # Bestellung erstellen
    order = Order(customer, cart.products)
    print(order.order_confirmation())

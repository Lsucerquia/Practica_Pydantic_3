from models import Product

class ProductDatabase:
    def __init__(self):
        self.products = {}
        self.next_id = 1

    def create_product(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        product = Product(self.next_id, name, price, quantity)
        self.products[self.next_id] = product
        self.next_id += 1
        return product

    def read_product(self, product_id):
        product = self.products.get(product_id)
        if product is None:
            raise KeyError(f"Product with ID {product_id} not found.")
        return product

    def update_product(self, product_id, name=None, price=None, quantity=None):
        product = self.products.get(product_id)
        if product is None:
            raise KeyError(f"Product with ID {product_id} not found.")
        
        if name is not None:
            product.name = name
        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative.")
            product.price = price
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity must be non-negative.")
            product.quantity = quantity
        
        return product

    def delete_product(self, product_id):
        product = self.products.pop(product_id, None)
        if product is None:
            raise KeyError(f"Product with ID {product_id} not found.")
        return product

    def list_products(self):
        return list(self.products.values())
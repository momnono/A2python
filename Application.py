"""methods for creating a product instance, simulating the monthly production and sale of the product, and generating the predicted stock statement."""
from Product import Product
import StockStatement

class Application:
    def __init__(self):
        self.products = []
        self.statements = []

    def create_product(self, code, name, price, cost, stock):
        product = Product(code, name, price, cost, stock)
        self.products.append(product)
        return product

    def sell_product(self, product_code, qty):
        product = self.get_product(product_code)
        if product:
            revenue = product.sell(qty)
            if revenue > 0:
                statement = self.get_statement(product)
                statement.add_sale(qty - int(revenue / product.price))
                return revenue
        return 0


    def restock_product(self, product_code, qty):
        product = self.get_product(product_code)
        if product:
            product.restock(qty)

    def predict_stock(self, product_code):
        product = self.get_product(product_code)
        if product:
            return product.predict_stock()
        return ""

    def get_product(self, product_code):
        for product in self.products:
            if product.code == product_code:
                return product
        print("Product not found!")
        return None

    def get_statement(self, product):
        for statement in self.statements:
            if statement.product == product:
                return statement
        statement = StockStatement(product)
        self.statements.append(statement)
        return statement

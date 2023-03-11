"""attributes for the product object and an array to store the predicted monthly stock for the next 12 months."""
class Statement:
    def __init__(self, product):
        self.product = product
        self.total_sold = 0
        self.total_profit = 0

    def add_sale(self, units_sold):
        revenue = units_sold * self.product.sale_price
        cost = units_sold * self.product.manufacture_cost
        profit = revenue - cost

        self.total_sold += units_sold
        self.total_profit += profit

    def print_statement(self):
        print(f"Sales statement for product {self.product.code}:")
        print(f"Total units sold: {self.total_sold}")
        print(f"Total profit: {self.total_profit:.2f}")

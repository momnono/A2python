"""attributes for product code, product name, sale price, manufacture cost, stock level, and estimated monthly units manufactured. It should also have methods for calculating the total units sold, the net profit, and for simulating the monthly production and sale of the product"""
import random

class Product:
    def __init__(self, code, name, price, cost, stock):
        self.code = code
        self.name = name
        self.price = price
        self.cost = cost
        self.stock = stock
        
    def sell(self, qty):
        if qty > self.stock:
            print("Not enough stock!")
            return 0
        else:
            self.stock -= qty
            return self.price * qty
    
    def restock(self, qty):
        self.stock += qty
        
    def predict_stock(self):
        monthly_sold = random.randint(5, 15)
        monthly_made = monthly_sold + random.randint(-5, 5)
        net_profit = (self.price - self.cost) * monthly_sold
        
        report = f"Product Code: {self.code}\nProduct Name: {self.name}\nCurrent Stock: {self.stock}\n"
        report += "Predicted Monthly Stock for the next 12 months:\n"
        
        for month in range(1, 13):
            report += f"Month {month}: "
            report += f"Units Sold: {monthly_sold}, "
            report += f"Units Made: {monthly_made}, "
            report += f"Net Profit/Loss: {net_profit}\n"
            
            self.stock += monthly_made - monthly_sold
            monthly_sold = random.randint(5, 15)
            monthly_made = monthly_sold + random.randint(-5, 5)
            net_profit = (self.price - self.cost) * monthly_sold
        
        return report

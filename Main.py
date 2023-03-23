"""interacts with the user and acts ads the user interface"""

from Application import Application
from input_validation import input_int, input_float

app = Application()

while True:
    print("1. Create Product")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. Predict Stock")
    print("5. Quit")

    choice = input_int("Enter your choice: ")

    if choice == 1:
        code = input_int("Enter product code: ")
        name = input("Enter product name: ")
        price = input_float("Enter product price: ")
        cost = input_float("Enter product cost: ")
        stock = input_int("Enter product stock: ")
        app.create_product(code, name, price, cost, stock)
        print("Product created successfully!")

    elif choice == 2:
        code = input_int("Enter product code: ")
        qty = input_int("Enter quantity: ")
        revenue = app.sell_product(code, qty)
        if revenue > 0:
            print(f"Sold {qty} units for ${revenue:.2f}")
        else:
            print("Failed to sell product.")

    elif choice == 3:
        code = input_int("Enter product code: ")
        qty = input_int("Enter quantity: ")
        app.restock_product(code, qty)
        print("Product restocked successfully!")

    elif choice == "4":
        code = input("Enter product code: ")
        report = app.predict_stock(code)
        statement = app.get_statement(app.get_product(code))
        unfulfilled_sales = statement.total_sold
        print(report)
        if unfulfilled_sales > 0:
            print(f"Unfulfilled sales: {unfulfilled_sales} units")

    elif choice == 5:
        break

    else:
        print("Invalid choice. Please try again.")

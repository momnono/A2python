"""interacts with the user and acts ads the user interface"""

from Application import Application


app = Application()

while True:
    print("1. Create Product")
    print("2. Sell Product")
    print("3. Restock Product")
    print("4. Predict Stock")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pass

    elif choice == "2":
        pass

    elif choice == "3":
        pass
    elif choice == "4":
        pass

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

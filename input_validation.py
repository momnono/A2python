'''module to ensure that the user inputs are of the correct data type'''
def input_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Please enter a valid integer.")

def input_float(prompt):
    while True:
        value = input(prompt)
        if value.replace('.', '', 1).isdigit():
            return float(value)
        else:
            print("Please enter a valid number.")

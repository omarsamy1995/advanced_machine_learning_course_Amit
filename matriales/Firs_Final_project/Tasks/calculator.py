class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    def perform_calculation(self, operation, num1, num2):
        if operation == '1':
            return self.add(num1, num2)
        elif operation == '2':
            return self.subtract(num1, num2)
        elif operation == '3':
            return self.multiply(num1, num2)
        elif operation == '4':
            return self.divide(num1, num2)
        else:
            return "Invalid operation"

    def run(self):
        print("Welcome to the calculator!")
        print("Choose an operation:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")

        operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        if operation in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                return

            result = self.perform_calculation(operation, num1, num2)
            if isinstance(result, str):
                print(result)  # Prints error message for division by zero
            else:
                operations = {'1': '+', '2': '-', '3': '*', '4': '/'}
                print(f"{num1} {operations[operation]} {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")


calculator = Calculator()
calculator.run()

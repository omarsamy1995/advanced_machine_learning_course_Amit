def mean():
    print("Welcome to my Calculator")
    
    while True:  # Keep the calculator running in a loop
        print("Select an operation:")
        print("1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(*)\n4. Division(/)")
        operator = input("Enter your choice (1,2,3,4) or type 'exit' to quit: ").lower()

        if operator == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        # Input validation for operator
        if operator not in ['1', '2', '3', '4']:
            print("Invalid operator. Please try again.")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Define the operations
        def addition(num1, num2):
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        def subtraction(num1, num2):
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        def multiplication(num1, num2):
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        def division(num1, num2):
            try:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

        # Call the appropriate operation function
        if operator == '1':
            addition(num1, num2)
        elif operator == '2':
            subtraction(num1, num2)
        elif operator == '3':
            multiplication(num1, num2)
        elif operator == '4':
            division(num1, num2)

# Run the calculator
mean()

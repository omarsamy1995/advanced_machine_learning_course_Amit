class Calculator1:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def summation(self):
        return self.n1 + self.n2

    def subtraction(self):
        return self.n1 - self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def division(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Error! Division by zero."

class Calculator2(Calculator1):
    def power(self):
        return self.n1 ** self.n2

while True:
    n1 = int(input("Enter number one: "))
    n2 = int(input("Enter second number: "))
    c = Calculator2(n1, n2)
    
    operator = input("Choose your operator (+, -, *, /, **). Type 'exit' to quit: ")
    
    if operator == "+":
        print(f"Result: {c.summation()}")
    elif operator == "-":
        print(f"Result: {c.subtraction()}")
    elif operator == "*":
        print(f"Result: {c.multiplication()}")
    elif operator == "/":
        print(f"Result: {c.division()}")
    elif operator == "**":
        print(f"Result: {c.power()}")
    elif operator == "exit":
        print("Thank you for using my calculator.")
        break
    else:
        print("Invalid operator, please try again.")

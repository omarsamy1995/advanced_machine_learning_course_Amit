import tkinter as tk
from tkinter import messagebox

# Define the calculator class with GUI using Tkinter
def mean():
    # Create the main window
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("300x400")

    # Global variables to store numbers and operator
    num1 = tk.StringVar()
    num2 = tk.StringVar()
    operator = tk.StringVar()

    # Functions for each operation
    def addition():
        try:
            result = float(num1.get()) + float(num2.get())
            messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def subtraction():
        try:
            result = float(num1.get()) - float(num2.get())
            messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def multiplication():
        try:
            result = float(num1.get()) * float(num2.get())
            messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def division():
        try:
            divisor = float(num2.get())
            if divisor == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
            else:
                result = float(num1.get()) / divisor
                messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    # Create the GUI layout
    tk.Label(window, text="First Number").pack(pady=10)
    tk.Entry(window, textvariable=num1).pack()

    tk.Label(window, text="Second Number").pack(pady=10)
    tk.Entry(window, textvariable=num2).pack()

    tk.Label(window, text="Select an operation").pack(pady=10)

    # Buttons for each operation
    tk.Button(window, text="Addition (+)", command=addition).pack(pady=5)
    tk.Button(window, text="Subtraction (-)", command=subtraction).pack(pady=5)
    tk.Button(window, text="Multiplication (*)", command=multiplication).pack(pady=5)
    tk.Button(window, text="Division (/)", command=division).pack(pady=5)

    # Exit button
    tk.Button(window, text="Exit", command=window.quit).pack(pady=20)

    # Run the GUI loop
    window.mainloop()

# Run the GUI calculator
mean()

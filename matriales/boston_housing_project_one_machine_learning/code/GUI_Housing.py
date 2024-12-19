import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Load and preview data
def load_data():
    file_path = filedialog.askopenfilename(title="Select a CSV File", filetypes=[("CSV files", "*.csv")])
    if file_path:
        global data
        data = pd.read_csv(file_path)
        messagebox.showinfo("Success", "Data loaded successfully!")
        preview_data()

def preview_data():
    if 'data' in globals():
        
        for row in preview_tree.get_children():
            preview_tree.delete(row)


        preview_tree["columns"] = list(data.columns)
        for col in data.columns:
            preview_tree.heading(col, text=col)
            preview_tree.column(col, width=100)
            
        # Preview first 10 rows
        for _, row in data.head(10).iterrows(): 
            preview_tree.insert("", "end", values=list(row))
    else:
        messagebox.showerror("Error", "No data to preview. Please load the data first.")

def plot_data():
    if 'data' not in globals():
        messagebox.showerror("Error", "Please load the data first.")
        return

    col = plot_column.get()
    if col not in data.columns:
        messagebox.showerror("Error", "Invalid column selected.")
        return

    plt.figure(figsize=(8, 5))
    if plot_type.get() == "Histogram":
        data[col].hist(bins=30)
        plt.title(f"Histogram of {col}")
    elif plot_type.get() == "Scatter":
        target_col = target_column.get()
        if target_col not in data.columns:
            messagebox.showerror("Error", "Invalid target column.")
            return
        plt.scatter(data[col], data[target_col])
        plt.title(f"Scatter plot of {col} vs {target_col}")
        plt.xlabel(col)
        plt.ylabel(target_col)
    plt.show()

def run_analysis():
    try:
        if 'data' not in globals():
            raise ValueError("Please load the data first.")

        target_col = target_column.get()
        if target_col not in data.columns:
            raise ValueError("Invalid target column.")

        X = data.drop(columns=[target_col])
        y = data[target_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model_type = model_choice.get()
        if model_type == "Linear Regression":
            model = LinearRegression()
        elif model_type == "Ridge Regression":
            model = Ridge(alpha=1.0)
        elif model_type == "Lasso Regression":
            model = Lasso(alpha=0.1)
        else:
            raise ValueError("Invalid model selected.")

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        result_label.config(text=f"MSE: {mse:.2f}, R2: {r2:.2f}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Boston Housing ")

# Load data
load_button = tk.Button(root, text="Load Data", command=load_data)
load_button.pack(pady=10)

# Preview data table
preview_frame = tk.Frame(root)
preview_frame.pack(pady=10)
preview_tree = ttk.Treeview(preview_frame, columns=[], show="headings", height=10)
preview_tree.pack()

# Plot options
plot_column = tk.StringVar()
plot_type = tk.StringVar(value="Histogram")
plot_frame = tk.Frame(root)
plot_frame.pack(pady=10)

tk.Label(plot_frame, text="Column to Plot:").grid(row=0, column=0)
tk.Entry(plot_frame, textvariable=plot_column).grid(row=0, column=1)

tk.Label(plot_frame, text="Plot Type:").grid(row=1, column=0)
ttk.Combobox(plot_frame, textvariable=plot_type, values=["Histogram", "Scatter"]).grid(row=1, column=1)

plot_button = tk.Button(root, text="Plot Data", command=plot_data)
plot_button.pack(pady=10)

# Model options
model_choice = tk.StringVar(value="Linear Regression")
model_frame = tk.Frame(root)
model_frame.pack(pady=10)

tk.Label(model_frame, text="Model:").grid(row=0, column=0)
ttk.Combobox(model_frame, textvariable=model_choice, values=["Linear Regression", "Ridge Regression", "Lasso Regression"]).grid(row=0, column=1)

target_column = tk.StringVar()
tk.Label(model_frame, text="Target Column:").grid(row=1, column=0)
tk.Entry(model_frame, textvariable=target_column).grid(row=1, column=1)

# Run analysis
run_button = tk.Button(root, text="Run Analysis", command=run_analysis)
run_button.pack(pady=10)

result_label = tk.Label(root, text="Results will appear here.")
result_label.pack(pady=20)

# Run the application
root.mainloop()

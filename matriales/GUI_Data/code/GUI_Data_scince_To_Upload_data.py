import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize Tkinter window
root = tk.Tk()
root.title("Data Science Final Project GUI")
root.geometry("800x600")

# Global variable to hold dataset
data = None

def load_file():
    """Load a CSV file."""
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    try:
        data = pd.read_csv(file_path)
        messagebox.showinfo("File Loaded", f"File loaded successfully: {file_path}")
        display_preview()
    except Exception as e:
        messagebox.showerror("Error", f"Could not load file: {e}")

def display_preview():
    """Display a preview of the dataset."""
    if data is None:
        messagebox.showwarning("No Data", "Please load a dataset first.")
        return
    
    preview_window = tk.Toplevel(root)
    preview_window.title("Dataset Preview")
    
    text_widget = tk.Text(preview_window, wrap="none", height=20, width=80)
    text_widget.pack(expand=True, fill="both")
    text_widget.insert("1.0", data.head().to_string())
    text_widget.configure(state="disabled")

def show_summary():
    """Show summary statistics of the dataset."""
    if data is None:
        messagebox.showwarning("No Data", "Please load a dataset first.")
        return
    
    summary_window = tk.Toplevel(root)
    summary_window.title("Dataset Summary")
    
    text_widget = tk.Text(summary_window, wrap="none", height=20, width=80)
    text_widget.pack(expand=True, fill="both")
    text_widget.insert("1.0", data.describe().to_string())
    text_widget.configure(state="disabled")

def plot_heatmap():
    """Plot a heatmap of the correlation matrix."""
    if data is None:
        messagebox.showwarning("No Data", "Please load a dataset first.")
        return
    
    numeric_data = data.select_dtypes(include=["number"])
    if numeric_data.empty:
        messagebox.showerror("Error", "No numeric columns found for correlation.")
        return
    
    correlation_matrix = numeric_data.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

def scatter_plot():
    """Plot a scatter plot based on user input."""
    if data is None:
        messagebox.showwarning("No Data", "Please load a dataset first.")
        return
    
    scatter_window = tk.Toplevel(root)
    scatter_window.title("Scatter Plot")
    
    # Dropdown menus for selecting columns
    col1_label = tk.Label(scatter_window, text="Select X-axis:")
    col1_label.pack()
    x_col_var = tk.StringVar(scatter_window)
    x_col_menu = tk.OptionMenu(scatter_window, x_col_var, *data.columns)
    x_col_menu.pack()
    
    col2_label = tk.Label(scatter_window, text="Select Y-axis:")
    col2_label.pack()
    y_col_var = tk.StringVar(scatter_window)
    y_col_menu = tk.OptionMenu(scatter_window, y_col_var, *data.columns)
    y_col_menu.pack()
    
    def generate_scatter():
        x_col = x_col_var.get()
        y_col = y_col_var.get()
        if not x_col or not y_col:
            messagebox.showwarning("Error", "Please select both X and Y columns.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.scatter(data[x_col], data[y_col], alpha=0.5, color="blue")
        plt.title(f"Scatter Plot: {x_col} vs {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()
    
    generate_button = tk.Button(scatter_window, text="Generate Plot", command=generate_scatter)
    generate_button.pack()

# Buttons
load_button = tk.Button(root, text="Load CSV File", command=load_file)
load_button.pack(pady=10)

preview_button = tk.Button(root, text="Preview Dataset", command=display_preview)
preview_button.pack(pady=10)

summary_button = tk.Button(root, text="Show Summary", command=show_summary)
summary_button.pack(pady=10)

heatmap_button = tk.Button(root, text="Plot Heatmap", command=plot_heatmap)
heatmap_button.pack(pady=10)

scatter_button = tk.Button(root, text="Scatter Plot", command=scatter_plot)
scatter_button.pack(pady=10)

# Add an Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Run Tkinter main loop
root.mainloop()

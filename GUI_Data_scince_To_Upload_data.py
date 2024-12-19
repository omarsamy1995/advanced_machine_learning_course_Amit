import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, r2_score
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class DataScienceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Data Science GUI")
        self.root.geometry("1000x700")

        # Global variables
        self.data = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
        self.selected_model = None

        # Notebook tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")

        self.create_tabs()

    def create_tabs(self):
        # Tab 1: Load and Preview Data
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Load & Preview Data")
        self.load_data_tab()

        # Tab 2: Preprocess Data
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Preprocess Data")
        self.preprocess_data_tab()

        # Tab 3: Select and Train Model
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Select & Train Model")
        self.model_tab()

        # Tab 4: Results
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Results")
        self.results_tab()

    def load_data_tab(self):
        load_frame = ttk.LabelFrame(self.tab1, text="Load Dataset")
        load_frame.pack(fill="x", padx=10, pady=10)

        load_button = ttk.Button(load_frame, text="Load CSV File", command=self.load_file)
        load_button.pack(pady=10)

        preview_frame = ttk.LabelFrame(self.tab1, text="Data Preview")
        preview_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.preview_text = tk.Text(preview_frame, wrap="none", height=20)
        self.preview_text.pack(fill="both", expand=True)
        
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            self.data = pd.read_csv(file_path)
            self.preview_text.delete("1.0", tk.END)
            self.preview_text.insert("1.0", self.data.head().to_string())
            messagebox.showinfo("File Loaded", f"File loaded successfully: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load file: {e}")

    def preprocess_data_tab(self):
        preprocess_frame = ttk.LabelFrame(self.tab2, text="Preprocess Data")
        preprocess_frame.pack(fill="x", padx=10, pady=10)

        process_button = ttk.Button(preprocess_frame, text="Preprocess Data", command=self.preprocess_data)
        process_button.pack(pady=10)

    def preprocess_data(self):
        if self.data is None:
            messagebox.showwarning("No Data", "Please load a dataset first.")
            return

        # Automatically handle missing values and select numeric columns
        self.data = self.data.select_dtypes(include=[np.number]).fillna(0)
        
        target_window = tk.Toplevel(self.root)
        target_window.title("Select Target Column")
        tk.Label(target_window, text="Select the target column:").pack()

        target_var = tk.StringVar(target_window)
        target_menu = ttk.OptionMenu(target_window, target_var, *self.data.columns)
        target_menu.pack()

        def set_target():
            target_col = target_var.get()
            if not target_col:
                messagebox.showwarning("Error", "Please select a target column.")
                return
            try:
                X = self.data.drop(columns=[target_col])
                y = self.data[target_col]
                self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                messagebox.showinfo("Success", "Data preprocessed successfully!")
                target_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error in preprocessing: {e}")

        submit_button = ttk.Button(target_window, text="Confirm Target", command=set_target)
        submit_button.pack()

    def model_tab(self):
        model_frame = ttk.LabelFrame(self.tab3, text="Choose Model")
        model_frame.pack(fill="x", padx=10, pady=10)

        self.model_var = tk.StringVar(value="Linear Regression")
        models = ["Linear Regression", "Logistic Regression", "SVM", "Random Forest"]
        
        for model in models:
            rb = ttk.Radiobutton(model_frame, text=model, variable=self.model_var, value=model)
            rb.pack(anchor="w")

        train_button = ttk.Button(self.tab3, text="Train Model", command=self.train_and_evaluate_model)
        train_button.pack(pady=10)

    def train_and_evaluate_model(self):
        if self.X_train is None or self.y_train is None:
            messagebox.showwarning("No Data", "Please preprocess the data first.")
            return

        try:
            selected_model = self.model_var.get()
            if selected_model == "Linear Regression":
                model = LinearRegression()
                model.fit(self.X_train, self.y_train)
                y_pred = model.predict(self.X_test)
                r2 = r2_score(self.y_test, y_pred)
                self.display_results(f"R-squared: {r2:.2f}")
            elif selected_model == "Logistic Regression":
                model = LogisticRegression(max_iter=1000)
                model.fit(self.X_train, self.y_train)
                y_pred = model.predict(self.X_test)
                acc = accuracy_score(self.y_test, y_pred)
                f1 = f1_score(self.y_test, y_pred, average='weighted')
                self.display_results(f"Accuracy: {acc:.2f}\nF1 Score: {f1:.2f}")
            elif selected_model == "SVM":
                model = SVC()
                model.fit(self.X_train, self.y_train)
                y_pred = model.predict(self.X_test)
                acc = accuracy_score(self.y_test, y_pred)
                self.display_results(f"Accuracy: {acc:.2f}")
            elif selected_model == "Random Forest":
                model = RandomForestClassifier()
                model.fit(self.X_train, self.y_train)
                y_pred = model.predict(self.X_test)
                acc = accuracy_score(self.y_test, y_pred)
                f1 = f1_score(self.y_test, y_pred, average='weighted')
                self.display_results(f"Accuracy: {acc:.2f}\nF1 Score: {f1:.2f}")
        except Exception as e:
            messagebox.showerror("Error", f"Model training failed: {e}")

    def display_results(self, result_text):
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert("1.0", result_text)

    def results_tab(self):
        results_frame = ttk.LabelFrame(self.tab4, text="Model Results")
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.results_text = tk.Text(results_frame, wrap="word", height=15)
        self.results_text.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataScienceGUI(root)
    root.mainloop()

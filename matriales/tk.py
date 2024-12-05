import pandas as pd
from tkinter import *
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("D:/diploma AI/advanced_machine_learning_course_Amit/matriales/Machine_learning/code/Salary_Data.csv")
X = df[['YearsExperience']]  
y = df['Salary']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# إعداد واجهة Tkinter
class SalaryPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("AMIT - Machine Learning Diploma")
        self.root.configure(bg="white")
        

        # title
        title = Label(self.root, text="Amit-Machine Learning Diploma",  compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        lbl_years = Label(self.root, text="Enter years of experience:", font=("Arial", 15, "bold"), bg="white", fg="black")
        lbl_years.place(x=300, y=150)
        
        self.experience_var = StringVar()
        txt_years = Entry(self.root, textvariable=self.experience_var, font=("Arial", 15), bg="lightyellow")
        txt_years.place(x=300, y=200, width=200)

        btn_predict = Button(self.root, text="Execute", font=("Arial", 15, "bold"), bg="black", fg="white", command=self.predict_salary)
        btn_predict.place(x=350, y=250)

        self.lbl_result = Label(self.root, text="", font=("Arial", 15, "bold"), bg="white", fg="green")
        self.lbl_result.place(x=300, y=300)

    def predict_salary(self):
        try:
            years = float(self.experience_var.get())
            predicted_salary = model.predict([[years]])[0]
            self.lbl_result.config(text=f"Your Expected Salary is: {int(predicted_salary)}")
        except ValueError:
            self.lbl_result.config(text="Please enter a valid number!", fg="red")

if __name__ == "__main__":
    root = Tk()
    app = SalaryPredictionApp(root)
    root.mainloop()

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def to_dict(self):
        return {"name": self.name, "age": self.age}


class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_info(self):
        super().view_info()
        print(f"Medical Record: {self.medical_record}")

    def to_dict(self):
        data = super().to_dict()
        data["medical_record"] = self.medical_record
        return data


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        super().view_info()
        print(f"Position: {self.position}")

    def to_dict(self):
        data = super().to_dict()
        data["position"] = self.position
        return data


class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to the {self.name} department.")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Staff '{staff.name}' added to the {self.name} department.")

    def to_dict(self):
        return {
            "name": self.name,
            "patients": [patient.to_dict() for patient in self.patients],
            "staff": [staff.to_dict() for staff in self.staff]
        }


class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name} Hospital.")

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "departments": [department.to_dict() for department in self.departments]
        }

    def save_to_json(self, filename="hospital_data.json"):
        """Save the hospital data to a JSON file."""
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, indent=4)
        print(f"Data saved to {filename}.")


# Creating Hospital instance with inputs
hospital_name = input("Enter the hospital name: ")
hospital_location = input("Enter the hospital location: ")
hospital = Hospital(hospital_name, hospital_location)

# Creating a Department
dept_name = input("Enter the department name: ")
department = Department(dept_name)
hospital.add_department(department)

# Creating a Patient
patient_name = input("Enter patient's name: ")
patient_age = int(input("Enter patient's age: "))
medical_record = input("Enter patient's medical record: ")
patient = Patient(patient_name, patient_age, medical_record)
department.add_patient(patient)

# Creating a Staff member
staff_name = input("Enter staff member's name: ")
staff_age = int(input("Enter staff member's age: "))
position = input("Enter staff member's position: ")
staff = Staff(staff_name, staff_age, position)
department.add_staff(staff)

# Viewing added info
print("\n--- Hospital Information ---")
print(f"Hospital Name: {hospital.name}")
print(f"Location: {hospital.location}")

print("\n--- Department Information ---")
print(f"Department Name: {department.name}")

print("\n--- Patient Information ---")
patient.view_info()

print("\n--- Staff Information ---")
staff.view_info()

# Save all data to JSON
hospital.save_to_json()

import json

#  Define a Student class
class Student:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

    def __str__(self):
        return f"{self.F_Name} , {self.L_Name} : ID = {self.Student_ID} , Email = {self.Email}"

# Load JSON into Python class list
def load_students_from_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return [Student(**student) for student in data]
    
# Save updated student list to the JSON file
def save_students_to_json(file_name, students):
    with open(file_name, "w") as file:
        # Convert the student objects to dictionaries before dumping them
        data = [{"F_Name": student.F_Name, "L_Name": student.L_Name, "Student_ID": student.Student_ID, "Email": student.Email} for student in students]
        json.dump(data, file, indent=4)
        print("The .json file has been successfully updated.") 
    
# Notify the  user about the original list
def print_student_list(students, is_updated=False):
    if is_updated:
        print("This is the updated Students list:\n")
    else:
        print("This is the original Student list:\n")

    for student in students:
        print(student)

#  Use the function and print each student
file_name = "C:/Users/samir/Downloads/student.json"
students = load_students_from_json(file_name)

# Notify user original list
print_student_list(students)

# Adding new student
my_student = Student("Samir", "Rodriguez", 11472, "elvaliente9@gmail.com")
students.append(my_student) # Append new student

# Notify the updated list
print_student_list(students, is_updated=True)

# Save the updated list back to the JSON file
save_students_to_json(file_name, students)
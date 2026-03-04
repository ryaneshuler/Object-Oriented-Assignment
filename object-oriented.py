# Simple example demonstrating a Student class and operations on student objects
# - Defines a Student class (name, email, grades)
# - Creates three Student instances
# - Provides helper functions that operate on Student instances
# - Stores students in a dictionary keyed by email

class Student:
    # Student class represents a single student with name, email, and a list of grades
    def __init__(self, name, email, grades=None):
        self.name = name
        self.email = email
        self.grades = grades if grades is not None else []

# Student instances (objects) — these are concrete students you can work with
Student1 = Student(
    name='John Doe',
    email='john.doe@example.com',
    grades=[85, 93, 78]
)

Student2 = Student(
    name='Jane Smith',
    email='jane.smith@example.com',
    grades=[88, 92, 80]
)

Student3 = Student(
    name='Emily Johnson',
    email='emily.johnson@example.com',
    grades=[95, 89, 84]
)

# Helper functions that operate on Student objects (defined as standalone functions here)
# In a more idiomatic OOP style these could be methods on the Student class.

def add_grade(self, grade):
    # Append a single grade to the student's grades list
    self.grades.append(grade)


def average_grade(self):
    # Compute the average grade for a student (return 0 if no grades)
    return sum(self.grades) / len(self.grades) if self.grades else 0


def display_info(self):
    # Print basic information about the student and their average
    print(f"Name: {self.name}")
    print(f"Email: {self.email}")
    print(f"Grades: {self.grades}")
    print(f"Average Grade: {average_grade(self)}")

# Add some example grades to each student using the helper function
for g in (88, 90):
    add_grade(Student1, g)

for g in (85, 87):
    add_grade(Student2, g)

for g in (90, 92):
    add_grade(Student3, g)

# Show information for each student
display_info(Student1)
display_info(Student2)
display_info(Student3)

# Dictionary mapping: email (key) -> Student instance (value)
# This allows quick lookup of a student by their email address
student_dict = {
    'john.doe@example.com': Student1,
    'jane.smith@example.com': Student2,
    'emily.johnson@example.com': Student3
}

def get_student_by_email(email):
    # Return the Student object for the given email, or None if not found
    return student_dict.get(email)

# Collect all unique grades across all students
unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)
print(f"All unique grades: {unique_grades}")

# Utility functions working with a Student object

def grades_tuple(self):
    # Return the student's grades as an immutable tuple
    return tuple(self.grades)


def remove_last_grade(self):
    # Remove the last grade from the student's grades list (if any)
    if self.grades:
        self.grades.pop()

# Remove the last grade from each student in the dictionary
for student in student_dict.values():
    remove_last_grade(student)

# Print the first and last grade for each student (if present)
for s in (Student1, Student2, Student3):
    if s.grades:
        print(f"{s.name} first grade: {s.grades[0]}, last grade: {s.grades[-1]}")
    else:
        print(f"{s.name} has no grades")

# Print the number of grades a student has (if any)
for s in (Student1, Student2, Student3):
    if s.grades:
        print(f"{s.name} has {len(s.grades)} grades")

import re

# Validate each student's email address
def is_valid_email(email):
    # Simple regex for validating an email address
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# Check and print the validity of each student's email
for student in student_dict.values():
    if is_valid_email(student.email):
        print(f"{student.name}'s email is valid.")
    else:
        print(f"{student.name}'s email is invalid.")

# Count how many grades are above 90 across all students
high_achievers = []
for student in student_dict.values():
    if any(grade > 90 for grade in student.grades):
        high_achievers.append(student.name)

print(f"Students with grades above 90: {', '.join(high_achievers) if high_achievers else 'None'}") 


students = {
    "Rahul": 75,
    "Akash": 85,
    "Riya": 45,
    "Amit": 60,
    "Priya": 90
}

print("Student Marks:")

for name, marks in students.items():
    print(name, ":", marks)

print("Students scoring 50 or above:")

for name, marks in students.items():
    if marks >= 50:
        print(name)

highest = max(students.values())

print("Highest Mark:", highest)


name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input("Enter subject marks: "))
    marks.append(mark)

def calculate(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

total, average = calculate(marks)

if average >= 40:
    result = "Pass"
else:
    result = "Fail"

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)

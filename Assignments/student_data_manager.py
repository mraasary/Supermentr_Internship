"""Assignment (19/02/2026) 
   Assignment Name : Student Data Manager 
   Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades."""
   
students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Print the topper
topper = max(students, key=students.get)
print("\nTopper:", topper, "-", students[topper])

# Print class average
average = sum(students.values()) / len(students)
print("Class Average:", average)

# Assign grades based on marks
def grade(m):
    if m >= 90: return "A"
    elif m >= 80: return "B"
    elif m >= 70: return "C"
    else: return "D"

for name, marks in students.items():
    print(name, "Grade:", grade(marks))
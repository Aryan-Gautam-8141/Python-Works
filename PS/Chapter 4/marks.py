subjects = ["English", "Maths", "Science", "History", "Computer"]
marks = []

for i in range(5):
    value = int(input(f"Enter marks for {subjects[i]} : ")) # subjects[i] gives the name of each subject.
    marks.append(value)

print("\nMarks Summary :")
for subject, mark in zip(subjects, marks):  # zip(subjects, marks) combines both lists for printing together.
    print(f"{subject} : {mark}")

print("Total Marks:", sum(marks))
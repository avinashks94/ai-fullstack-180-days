employees = [
    {
        "name": "Avinash",
        "role": "Software Engineer",
        "experience": 2.5,
        "salary": 450000
    },
    {
        "name": "Vivek",
        "role": "Sr. Software Engineer",
        "experience": 5,
        "salary": 1050000
    },
    {
        "name": "Rahul",
        "role": "Programmer",
        "experience": 8,
        "salary": 1200000
    }
]

print('--- Employee List ---')
for employee in employees:
    print('Name:',employee['name'])
    print('Role:',employee['role'])
    print('Experience:',employee['experience'])
    print('Salary:',employee['salary'])



# ---------- Find Employee with highest experience ----------
highest_experience = employees[0]

for employee in employees:
    if employee["experience"] > highest_experience["experience"]:
        highest_experience = employee

print("Most Experienced:", highest_experience["name"])

# -----------------Challenge 1 — Unique Skills-------------
skills = [
    "Angular",
    "Laravel",
    "Python",
    "Angular",
    "MySQL",
    "Python"
]
unique_skills = set(skills)

print(unique_skills)

# --------------Challenge 2 — Numbers-------------
numbers = [10, 20, 30, 40, 50]

total=0
count=0
largest=numbers[0]
for number in numbers:
    total=total+number
    count=count+1
    if number>largest:
        largest=number

average=total/count
# or
average = total / len(numbers)

print(total)
print(average)
print(largest)


# -----------Challenge 3 — Dictionary----------
student = {
    "name": "Avinash",
    "age": 26,
    "course": "MCA",
    "marks": 90
}


print('Name:',student['name'])
print('Age:',student['age'])
print('Course:',student['course'])
print('Marks:',student['marks'])
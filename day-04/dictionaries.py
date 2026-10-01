
# --------------------Part 6 — Dictionary-----------------------

employee = {
    "name": "Avinash",
    "age": 29,
    "experience": 2.5,
    "role": "Software Engineer"
}
print(employee["name"])
print(employee["role"])

employee["experience"] = 3
print(employee["experience"])

employee["salary"] = 450000
print(employee["salary"])


del employee["age"]
# or
# employee.pop("age")
print(employee)

# --------------Dictionary Loop-----------
for key in employee:
    print(key)

for value in employee.values():
    print(value)

for key, value in employee.items():
    print(key, ":", value)


# ---------------Part 7 — Real-world Employee Data-----------

employee = {
    "name": "Avinash",
    "age": 29,
    "experience": 2.5,
    "role": "Software Engineer",
    "skills": ["Angular", "Laravel", "MySQL"]
}

print(employee)
print(employee["skills"])
print(employee["skills"][0])


# -------------------Part 8 — List of Dictionaries---------------

employees = [
    {
        "name": "Avinash",
        "role": "Software Engineer",
        "experience": 2.5
    },
    {
        "name": "Rahul",
        "role": "Developer",
        "experience": 3
    },
    {
        "name": "Neha",
        "role": "Tester",
        "experience": 2
    }
]

for employee in employees:
    print(employee["name"], "-", employee["role"])
# -------------Part 1 — List-----------------

employees = ["Avinash", "Rahul", "Amit", "Neha"]
print(employees)
print(employees[0])
print(employees[3])

#------------Part 2 — Modify List----------------

employees.append("Suresh")
employees.insert(1, "Priya")

print(employees)

employees.remove("Rahul")
employees.pop()
print(employees)
print(len(employees))

# -----------------Part 3 — List + Loop-----------------
employees = ["Avinash", "Rahul", "Amit", "Neha"]

for employee in employees:
    print(employee)


# ---------------Exercise 1------------
employees = ["Avinash", "Rahul", "Amit"]

employees.append("Neha")
employees.append("Suresh")
employees.append("Ravi")
employees.pop()

print("Total Employees:", len(employees))

for employee in employees:
    print(employee)





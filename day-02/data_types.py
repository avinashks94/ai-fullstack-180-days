# ------------Part 1 — Python Basic Data Types------------------------

name = "Avinash"
age = 29
experience = 2.5
salary=350000
is_software_engineer = True

print(type(name))
print(type(age))
print(type(experience))
print(type(salary))
print(type(is_software_engineer))

#----------------Part 2 — Arithmetic Operators---------------------

a=10
b=3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# ----------------Part 3 — Comparison Operators--------------

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#----------Part 4 — Logical Operators------------

age = 25
experience = 2

print(age >= 18 and experience >= 1)



age = 17
experience = 3

print(age >= 18 or experience >= 2)

# ---------------Part 5 — User Input-------------

name = input("Enter your name: ")

print("Hello", name)


age = input("Enter your age: ")

print(type(age))


# ---------------Part 6 — Type Conversion----------------

age = int(input("Enter your age: "))

salary = float(input("Enter your salary: "))
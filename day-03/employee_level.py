experience=float(input('Enter your experience:'))
if experience >= 5:
    print("Senior Developer")
elif experience >= 2:
    print("Mid-Level Developer")
else:
    print("Junior Developer")


# -------------Multiple Conditions--------------

age = int(input("Enter your age: "))
experience = float(input("Enter your experience: "))

if age >= 18 and experience >= 2:
    print("Eligible")
else:
    print("Not Eligible")

# ------------------Nested if---------------------

age = int(input("Enter your age: "))
experience = float(input("Enter your experience: "))

if age >= 18:

    if experience >= 2:
        print("Eligible for experienced position")
    else:
        print("Eligible for fresher position")

else:
    print("Not eligible")
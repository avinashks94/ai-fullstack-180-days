name = input("Enter your name: ")
age = int(input("Enter your age: "))
experience = float(input("Enter your experience: "))
annual_ctc = float(input("Enter your annual CTC: "))

monthly_ctc = annual_ctc / 12
experience_after_2_years = experience + 2

print("\n--- Employee Salary Report ---")

print("Name:", name)
print("Age:", age)
print("Experience:", experience, "years")

print("Annual CTC: ₹", annual_ctc)
print("Monthly CTC: ₹", f"{monthly_ctc:.2f}")

print("Experience after 2 years:", experience_after_2_years, "years")
# -------------Day 6 Main Challenge------------
# --------------Function 1----------------
def calculate_total_salary(*salaries):
    total=0
    for salary in salaries:
        total=total+salary

    return total

print(calculate_total_salary(450000, 600000, 750000))

# --------------------Function 2-------------------

def calculate_monthly_salary(salary):
    return salary/12


# --------------------Function 3-------------------

def calculate_average_salary(*salaries):
    total=calculate_total_salary(*salaries)
    average=total/len(salaries)
    return average
print(calculate_average_salary(450000, 600000, 750000))

# -------------------Function 4-------------------
def display_employee(**employee):
    print('Name:',employee['name'])
    print('Role:',employee['role'])
    print('Experience:',employee['experience'],'years')
    print('Current Salary:₹',employee['salary'])


# -----------------Function 5--------------------
def calculate_hike(salary, hike_percentage=10):
    return salary+(salary*hike_percentage/100)


# --------------------Function 6-------------------
def get_experience_level(experience):
    if(experience>=5):
        return 'Senior Developer'
    elif(experience>=2):
        return 'Mid-Level Developer'
    else:
        return 'Junior Developer'

# ----------------Bonus Challenge--------------
def employee_report(**employee):
    print("\n--- Employee Report ---")

    display_employee(**employee)

    new_salary = calculate_hike(
        employee['salary'],
        employee['hike_percentage']
    )

    monthly_salary = calculate_monthly_salary(new_salary)

    print("Hike:", employee['hike_percentage'], "%")
    print("New Salary: ₹", new_salary)
    print("Monthly Salary: ₹", monthly_salary)
    print("Level:", get_experience_level(employee['experience']))

employee_report(
    name="Avinash",
    role="Software Engineer",
    experience=2.5,
    salary=450000,
    hike_percentage=20
)
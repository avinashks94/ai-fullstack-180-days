# --------------------Function 1 — Employee Info------------

def display_employee(name, role, experience, salary):
    print('Name:',name)
    print('Role:',role)
    print('Experience:',experience)
    print('Annual Salary:',salary)



# ------------------Function 2 — Monthly Salary----------------
def calculate_monthly_salary(annual_salary):
    return annual_salary/12

# -----------------Function 3 — Experience Level-----------------
def get_experience_level(experience):
    if(experience>=5):
        return 'Senior Developer'
    elif(experience>=2):
        return 'Mid-Level Developer'
    else:
        return 'Junior Developer'


# ----------------Function 4 — Performance-------------
def get_performance(rating):
    if(rating==5):
        return 'Outstanding'
    elif(rating==4):
        return 'Excellent'
    elif(rating==3):
        return 'Good'
    elif(rating==2):
        return 'Needs Improvement'
    elif(rating==1):
        return 'Poor'
    else:
        return 'Invalid Rating'


print('--- Employee Report ---')
display_employee('Avinash','Software Engineer',2.5,450000)
print('Monthly salary:',calculate_monthly_salary(450000))
print('Level:',get_experience_level(2.5))
print('Performance:',get_performance(5))

# ------------------Bonus Challenge-----------------
def calculate_hike(salary, hike_percentage):
    return salary + (salary * hike_percentage / 100)


print("New Salary:",calculate_hike(450000, 20))
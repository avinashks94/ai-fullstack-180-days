name=input('Enter your name:')
age=int(input('Enter your age:'))
experience=float(input('Enter your Experience:'))
annualCtc=float(input('Enter your annual CTC:'))

monthlyCtc=annualCtc/12
expAfter2year=experience+2

print("\n--- Employee Salary Report ---")

print('Name:',name)
print('Age:',age)
print('Experience:',experience)

print('Annual CTC:',annualCtc)
print('Monthly CTC:',monthlyCtc)

print('Experience after 2 years:',expAfter2year)

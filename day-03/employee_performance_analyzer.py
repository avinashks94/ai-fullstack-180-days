name = input('Enter Name: ')
experience = float(input('Enter Experience: '))
per_rating = int(input('Enter Performance Rating: '))

performance = ''

if per_rating == 5:
    performance = 'Outstanding'
elif per_rating == 4:
    performance = 'Excellent'
elif per_rating == 3:
    performance = 'Good'
elif per_rating == 2:
    performance = 'Needs Improvement'
elif per_rating == 1:
    performance = 'Poor'
else:
    performance = 'Invalid Rating'

level = ''

if experience >= 5:
    level = 'Senior Developer'
elif experience >= 2:
    level = 'Mid-Level Developer'
else:
    level = 'Junior Developer'

print('--- Employee Performance Report ---')
print('Name:', name)
print('Experience:', experience)
print('Performance Rating:', per_rating)
print('Level:', level)
print('Performance:', performance)
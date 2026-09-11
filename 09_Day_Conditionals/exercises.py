# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# user_age = int(input('Enter your age: '))

# if user_age >= 18:
#     print('You are old enough to drive.')
# else:
#     print(f'You need {18 - user_age} more years to learn to drive.')

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# Enter your age: 30
# You are 5 years older than me.
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# my_age = 42
# your_age = int(input('Enter your age: '))

# if my_age > your_age:
#     print(f'You are {my_age - your_age} years older than me.')
# elif my_age < your_age:
#     print(f'You are {your_age - my_age} years older than me.')
# else:
#     print('We are of the same age.')

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
# student_score = int(input('Enter your score: '))
# if student_score >= 90 and student_score <= 100:
#     print('A')
# elif student_score >= 80 and student_score <= 89:
#     print('B')
# elif student_score >= 70 and student_score <= 79:
#     print('C')
# elif student_score >= 60 and student_score <= 69:
#     print('D')
# else:
#     print('F')
# # Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# month = input('Enter the month: ')
# autumn_months = ['September', 'October', 'November']
# winter_months = ['December', 'January', 'February']
# spring_months = ['March', 'April', 'May']
# summer_months = ['June', 'July', 'August']
# if month in autumn_months:
#     print('Autumn')
# elif month in winter_months:
#     print('Winter')
# elif month in spring_months:
#     print('Spring')



# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit_to_add = input('Enter the fruit to add: ')
# if fruit_to_add not in fruits:
#     fruits.append(fruit_to_add)
#     print(fruits)
# else:
#     print('That fruit already exist in the list')
# ```
# If a fruit doesn't exist in the list add the fruit to the list 
# and print the modified list. If the fruit exists 
# print('That fruit already exist in the list')


# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print(person['skills'][middle_index])
    if 'Python' in person['skills']:
        print('Yes, this person knows Python')
    elif 'Python' not in person['skills']:
        print('Bummer, this person does not know Python')
    elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('This person is a front end developer')
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('This person is a backend developer')
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
    elif 'Read' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('This person is a fullstack developer')
    else:
        print('unknown title')
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if person['is_married'] and person['country'] == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')
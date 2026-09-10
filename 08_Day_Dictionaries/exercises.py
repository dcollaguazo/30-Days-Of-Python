# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Sally'
dog['color'] = 'Black'
dog['breed'] = 'Mix'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Tomas',
    'last_name': 'Kral',
    'gender': 'male',
    'age': 30,
    'marital_status': 'single',
    'skills': ['Python', 'SQL', 'JavaScript'],
    'country': 'Czech Republic',
    'city': 'Prague',
    'address': '123 Main St, Prague, 12345'
}

# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
student['skills']
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('React')
student['skills'].append('Node.js')
print(student['skills'])
# Get the dictionary keys as a list
student_keys = list(student.keys())
print(student_keys)
# Get the dictionary values as a list
student_values = list(student.values())
print(student_values)
# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(student_items)
# Delete one of the items in the dictionary
student.popitem()
print(student)
# Delete one of the dictionaries
del student
# print(student)
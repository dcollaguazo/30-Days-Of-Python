import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.countries import countries
# ============================================================
# DAY 5 — LISTS
# ============================================================


# ============================================================
# EXERCISES — LEVEL 1
# ============================================================

# 1. Declare an empty list.
my_list = []

# 2. Declare a list with more than 5 items.
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple']

# 3. Find the length of your list.
print(len(fruits))

# 4. Get the first item, the middle item, and the last item
#    of the list.
print(fruits[::2])


# 5. Declare a list called mixed_data_types.
#    Put your:
#    - name
#    - age
#    - height
#    - marital status
#    - address
mixed_data_types = ['Daniela', 42, 1.59, 'Married', '123 Main St, Anytown, USA']

# 6. Declare a list variable named it_companies and assign
#    these initial values:
#    Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print().
print(it_companies)

# 8. Print the number of companies in the list.
print(len(it_companies))

# 9. Print the first, middle, and last company.
print(it_companies[::3])


# 10. Print the list after modifying one of the companies.
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies.
it_companies.append('Twitter')
print(it_companies)
# 12. Insert an IT company in the middle of the companies list.
middle_index = len(it_companies)//2
it_companies.insert(middle_index, 'Tesla')
print(it_companies)
# 13. Change one of the it_companies names to uppercase.
#     IBM is excluded!
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with the string '#;  '.
it_companies_string = '#;  '.join(it_companies)
print(it_companies_string)

# 15. Check if a certain company exists in the
#     it_companies list.
print('Netflix' in it_companies)

# 16. Sort the list using the sort() method.
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using
#     the reverse() method.
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list.
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list.
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies
#     from the list.
# it_companies with indexes:
#
# Index    Company
# -----    ---------
#   0      Twitter
#   1      Tesla
#   2      Oracle
#   3      Microsoft
#   4      META
#   5      IBM
#   6      Google
#   7      Apple
#   8      Amazon

middle_index = len(it_companies)//2

if len(it_companies) % 2 == 0:
    print(it_companies[middle_index-1:middle_index+1])
else:
    print(it_companies[middle_index:middle_index+1])



# 21. Remove the first IT company from the list.
del it_companies[0]
print(it_companies)

# 22. Remove the middle IT company or companies
#     from the list.
middle_index = len(it_companies)//2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index-1:middle_index+1]
    print(it_companies_string)
else:
    del it_companies[middle_index]
    print(it_companies)



# 23. Remove the last IT company from the list.
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list.
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list.
del it_companies

# 26. Join the following lists:
#
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_lists = front_end + back_end
print(joined_lists)

# 27. After joining the lists in question 26:
#     - Copy the joined list and assign it to a variable
#       called full_stack.
#     - Insert Python and SQL after Redux.

full_stack = joined_lists.copy()

to_insert = ['SQL', 'Python']
for item in to_insert:
    redux_index = full_stack.index('Redux')
    full_stack.insert(redux_index+1, item)
print(full_stack)

# ============================================================
# EXERCISES — LEVEL 2
# ============================================================

# 1. The following is a list of 10 students' ages:
#
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#
# a. Sort the list and find the minimum and maximum age.
ages.sort()
print(ages)
# b. Add the minimum age and maximum age again to the list.
sum_ages = int(ages[0]) + int(ages[-1])
print(sum_ages)
# c. Find the median age.
#    (One middle item, or two middle items divided by two.)
test_ages = [1, 2, 3, 4, 5]
test_ages_length = len(test_ages)
print(f'Test ages length: {test_ages_length}')
median = 0
middle_index = len(test_ages)//2
if test_ages_length % 2 == 0:
    median =  (int(test_ages[middle_index-1]) + int(test_ages[middle_index])) / 2
    print(f'Median: {median}')
else:
    median =  int(test_ages[middle_index])
    print(f'Median: {median}')
# d. Find the average age.
#    (Sum of all items divided by their number.)
average_age = sum(ages) / len(ages)
print(f'Average age: {average_age}')
# e. Find the range of the ages.    
#    (Maximum minus minimum.)
#
# f. Compare the values of:
#       min - average
#    and
#       max - average
#    using the abs() method.
max_age = max(ages)
min_age = min(ages)
range_age = max_age - min_age
print(f'Range of ages: {range_age}')
# 2. Find the middle country or countries in the countries list.
#
# The countries list comes from:
# data/countries.py
middle_index = len(countries)//2
if len(countries) % 2 == 0:
    print(countries[middle_index-1:middle_index+1])
else:
    print(countries[middle_index])

# 3. Divide the countries list into two equal lists.
#
#    If the number of countries is even:
#       - Both lists should have the same number of countries.
#
#    If the number is odd:
#       - The first half should contain one more country.
# countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
test_countries = countries[:4]
print(f'Test countries: {test_countries}')
length = print(f'Length of countries: {len(test_countries)}')
middle_index = len(test_countries)//2
print(f'Middle index: {middle_index}')
if len(test_countries) % 2 == 0:
    print(f'First half: {test_countries[0:middle_index]}')
    print(f'Second half: {test_countries[middle_index:]}')
else:
    print(f'First half: {test_countries[0:middle_index+1]}')
    print(f'Second half: {test_countries[middle_index+1:]}')

# 4. Given:
#
countries = [
    'China',
    'Russia',
    'USA',
    'Finland',
    'Sweden',
    'Norway',
    'Denmark'
]
#
# Unpack the first three countries into separate variables
# and unpack the rest as scandic countries.
chn, rus, usa, *scandic_countries = countries
print(f'China: {chn}')
print(f'Russia: {rus}')
print(f'USA: {usa}')
print(f'Scandic countries: {scandic_countries}')
import sys
from pathlib import Path
import json

path_str = str(Path(__file__).resolve().parent.parent)
sys.path.append(path_str)


from data.countries import countries

# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
# for i in range(11):
#     print(f'Printing this number {i} using for')

# j = 0
# while j <=10:
#     print(f'Printing this number {j} using while')
#     j+=1
# Iterate 10 to 0 using for loop, do the same using while loop.
# for i in range(10,-1,-1):
#     print(f'Printing this number {i} using for')

# j = 10
# while j >=0:
#     print(f'Printing this number {j} using while')
#     j-=1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# hashtag = '#'
# line = ''
# for i in range(8):
#     for j in range(i):
#         line += hashtag
#     print(line, end = "\n")
#     line = ''
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# Use nested loops to create the following:
# hashtag = '#'
# line =  ''
# i = 1
# for i in range(10):
#     for i in range(10):
#         line += hashtag + ' '
#     print(line)
#     line = ''
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# Print the following pattern:
# new_line = ''
# for i in range(11):
#     num = str(i)
#     square_num = str(i**2)
#     new_line += (num + ' x ' + num + ' = ' + square_num)
#     print(new_line)
#     new_line = ''

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
# for skill in skills:
#     print(skill)

# Use for loop to iterate from 0 to 100 and print only even numbers
# for i in range(101):
#     if i % 2 == 0:
#         print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
# for i in range(101):
#     if i % 2 != 0:
#         print(i)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
# sum_all = 0
# for i in range(101):
#     sum_all += i
# print(sum_all)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
# summ_evens = 0
# summ_odds = 0
# for i in range(101):
#     if i % 2 == 0:
#         summ_evens += i
#     else:
#         summ_odds+=i
# print(f'The sum of all even numbers from 0 to 100 is: {summ_evens} and the sum of all odd numbers from 0 - 100 is {summ_odds}')

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# pattern = 'land'
# countries_w_pattern = ''
# for country in countries:
#     if pattern in country:
#         countries_w_pattern+= country + '\n' 
# print(f'The countries that contain the string {pattern} are: \n {countries_w_pattern.strip()}')

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# fruits = ['banana', 'orange', 'mango', 'lemon'] 
# for fruit in range(-1,):
#     print(fruit)
# Go to the data folder and use the countries_data.py file.
countries_data_path = path_str + "/data/countries_data.json"
with open(countries_data_path, encoding="utf-8") as f:
    countries_data = json.load(f)

# print(countries_data)

# What are the total number of languages in the data
all_languages = []
countries_ds_ln = len(countries_data)

for i in range(countries_ds_ln):
    all_languages += countries_data[i]['languages']
total_languages = len(set(all_languages))
print((f'The total number of languages in the data set is {total_languages}'))

all_languages 

# Find the 10 most populated countries in the world
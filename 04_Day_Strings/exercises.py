# DAY 4 — STRINGS EXERCISES


# 1. Concatenate 'Thirty', 'Days', 'Of', and 'Python'
# into the single string 'Thirty Days Of Python'.

single_string = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(single_string)

# 2. Concatenate 'Coding', 'For', and 'All'
# into the single string 'Coding For All'.

single_string2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(single_string2)

# 3. Declare a variable named company and assign
# the initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company.
print(company)



# 5. Print the length of the company string using len().
length = len(company)
print(length)

# 6. Change all the characters in company to uppercase
# using upper().
print(company.upper())


# 7. Change all the characters in company to lowercase
# using lower().

print(company.lower())

# 8. Use capitalize(), title(), and swapcase() to format
# the string "Coding For All".

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Slice out the first word from the string "Coding For All".
print(company[0:6])



# 10. Check whether "Coding For All" contains the word "Coding".
# Use index(), find(), or another method.
if company.rfind('Coding') != -1:
    print('Coding For All contains the word "Coding"')
else:
    print('Coding For All does not contain the word "Coding"')

# 11. Replace "Coding" in "Coding For All" with "Python".
print(company.replace('Coding', 'Python'))


# 12. Change "Python for Everyone" to "Python for All"
# using replace() or another method.
str_to_replace = "Python for Everyone"
print(str_to_replace.replace('Everyone', 'All'))


# 13. Split "Coding For All" using a space as the separator.
print(company.split())


# 14. Split this string at the commas:
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_tech.split(','))


# 15. What is the character at index 0 in "Coding For All"?
first_letter = company[0]
print(first_letter)

# 16. What is the last index of the string "Coding For All"?
print(company[-1])


# 17. What character is at index 10 in "Coding For All"?
print(company[10])


# 18. Create an acronym/abbreviation for "Python For Everyone".
python_for_everyone = "Python For Everyone"
print(python_for_everyone.split()[0][0] + python_for_everyone.split()[1][0] + python_for_everyone.split()[2][0])

# 19. Create an acronym/abbreviation for "Coding For All".
coding_for_all = "Coding For All"
print(coding_for_all.split()[0][0] + coding_for_all.split()[1][0] + coding_for_all.split()[2][0])


# 20. Use index() to determine the position of the first
# occurrence of "C" in "Coding For All".
coding_for_all = "Coding For All"
print(coding_for_all.index('C'))


# 21. Use index() to determine the position of the first
# occurrence of "F" in "Coding For All".
print(coding_for_all.index('F'))


# 22. Use rfind() to determine the position of the last
# occurrence of "l" in "Coding For All People".
coding_for_all_people = "Coding For All People"
print(coding_for_all_people.rfind('l'))


# 23. Use index() or find() to find the position of the first
# occurrence of "because" in:
# "You cannot end a sentence with because because because is a conjunction"
because_sentence = "You cannot end a sentence with because because because is a conjunction"
print(because_sentence.index('because'))


# 24. Use rindex() to find the position of the last occurrence
# of "because" in:
# "You cannot end a sentence with because because because is a conjunction"
because_sentence = "You cannot end a sentence with because because because is a conjunction"
print(because_sentence.rindex('because'))


# 25. Slice out the phrase "because because because" from:
# "You cannot end a sentence with because because because is a conjunction"
to_remove = "because because because "
print(because_sentence.replace(to_remove, ''))



# 26. Find the position of the first occurrence of "because" in:
# "You cannot end a sentence with because because because is a conjunction"



# 27. Slice out the phrase "because because because" from:
# "You cannot end a sentence with because because because is a conjunction"



# 28. Does "Coding For All" start with the substring "Coding"?
if company.startswith('Coding'):
    print('Coding For All starts with the substring "Coding"')
else:
    print('Coding For All does not start with the substring "Coding"')


# 29. Does "Coding For All" end with the substring "coding"?
if company.endswith('Coding'):
    print('Coding For All starts with the substring "Coding"')
else:
    print('Coding For All does not start with the substring "Coding"')


# 30. Remove the leading and trailing spaces from:
# "   Coding For All      "
test_string = "   Coding For All      "
print(test_string.strip())


# 31. Which of these strings returns True with isidentifier()?
# "30DaysOfPython"
# "thirty_days_of_python"

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32. Given this list:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the items using a hash followed by a space ("# ").
print("# ".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))



# 33. Use the newline escape sequence to display:
#
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")


# 34. Use tab escape sequences to display:
#
# Name        Age     Country     City
# Asabeneh    250     Finland     Helsinki

print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# 35. Use string formatting to display the following result.
#
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')



# 36. Use string formatting to produce:
#
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
# 8 + 6 = 14
# 8 - 6 = 2
print(f'{a} - {b} = {a - b}')
# 8 * 6 = 48
print(f'{a} * {b} = {a * b}')
# 8 / 6 = 1.33
print(f'{a} / {b} = {a / b:.2f}')
# 8 % 6 = 2
print(f'{a} % {b} = {a % b}')
# 8 // 6 = 1
print(f'{a} // {b} = {a // b}')
# 8 ** 6 = 262144
print(f'{a} ** {b} = {a ** b}')
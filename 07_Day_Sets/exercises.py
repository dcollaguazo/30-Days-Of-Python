# Exercises: Level 1
# Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(f'Length of it_companies: {len(it_companies)}')

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f'It companies: {it_companies}')
# Insert multiple IT companies at once to the set it_companies

# Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(f'It companies: {it_companies}')

# What is the difference between remove and discard
# The difference between remove and discard is that remove will raise an error if the item is not found, while discard will not.

# Exercises: Level 2
# Join A and B
a= {1, 2, 3, 4, 5}
b= {3, 4, 5, 6, 7, 8}
print(a.union(b))
# Find A intersection B
print(a.intersection(b))
# Is A subset of B
print(a.issubset(b))
# Are A and B disjoint sets
print(a.isdisjoint(b))
# Join A with B and B with A
print(a.union(b))
print(b.union(a))


# What is the symmetric difference between A and B
print(f'Symmetric difference between A and B: {a.symmetric_difference(b)}')

# Delete the sets completely
del a, b
# Exercises: Level 3
# Convert the ages to a set and compare the 
# length of the list and the set, which one is bigger?
ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
ages_set = set(ages)
print(f'Length of ages list: {len(ages)}')
print(f'Length of ages set: {len(ages_set)}')

# Explain the difference between the following data types: string, list, tuple and set
# String is immutable, list is mutable, tuple is immutable, set is mutable.
# String is a squence of characters, list is an ordered collection of objects, tuple is an immutable ordered collection of objects, set is an unordered collection of objects.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
words_set = set(words)
print(f'Number of unique words: {len(words_set)}')
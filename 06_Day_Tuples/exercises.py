# ============================================================
# EXERCISES: DAY 6 — TUPLES
# ============================================================


# ------------------------------------------------------------
# EXERCISES: LEVEL 1
# ------------------------------------------------------------

# 1. Create an empty tuple.
empty_tuple = ( )
print(f'Empty tuple: {empty_tuple}')


# 2. Create a tuple containing names of your sisters and your
#    brothers. (Imaginary siblings are fine.)
sister_names = ('Jane', 'Jill')
brother_names = ('John', 'Jim')
# 3. Join the brothers and sisters tuples and assign the result
#    to a variable called siblings.
siblings = sister_names + brother_names
print(f'Siblings: {siblings}')



# 4. How many siblings do you have?
siblings_count = len(siblings)
print(f'Siblings count: {siblings_count}')

# 5. Modify the siblings tuple:
#    - Add the name of your father.
#    - Add the name of your mother.
#    - Assign the result to a variable called family_members.
father_name = 'John'
mother_name = 'Jane'
family_members = siblings + (father_name, mother_name)
print(f'Family members: {family_members}')


# ------------------------------------------------------------
# EXERCISES: LEVEL 2
# ------------------------------------------------------------

# 1. Unpack siblings and parents from family_members.
family_members_length = len(family_members)
print(f'Family members length: {family_members_length}')
siblings_tuple = family_members[0:family_members_length-2]
print(f'Siblings tuple: {siblings_tuple}')
parents_tuple = family_members[family_members_length-2:]
print(f'Parents tuple: {parents_tuple}')
# 2. Create three tuples:
#    - fruits
#    - vegetables
#    - animal_products
#
#    Join the three tuples and assign the result to a variable
#    called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'potato', 'onion')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(f'Food stuff tuple: {food_stuff_tp}')


# 3. Convert the food_stuff_tp tuple into a list and assign it
#    to a variable called food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)
print(f'Food stuff list: {food_stuff_lt}')

# 4. Slice out the middle item or items from either:
#    - food_stuff_tp
#    OR
#    - food_stuff_lt
food_stuff_lt_test = food_stuff_lt[:3]
food_stuff_lt_test_len = len(food_stuff_lt_test)
print(f'Food stuff list test: {food_stuff_lt_test}')
print(f'Food stuff list test length: {food_stuff_lt_test_len}')

if food_stuff_lt_test_len % 2 != 0:
    middle_item = food_stuff_lt_test[food_stuff_lt_test_len//2]
    print(f'Middle item: {middle_item}')
else:
    middle_items = food_stuff_lt_test[food_stuff_lt_test_len//2-1:food_stuff_lt_test_len//2+1]
    print(f'Middle items: {middle_items}')


# 5. Slice out:
#    - The first three items from food_stuff_lt.
#    - The last three items from food_stuff_lt.

print(f'Food stuff list first three: {food_stuff_lt[:3]}')
print(f'Food stuff list test last three: {food_stuff_lt[-3:]}')

# 6. Delete the food_stuff_tp tuple completely.
del food_stuff_tp


# 7. Check whether an item exists in a tuple.
#
#    Use:
#
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')


#    a. Check if 'Estonia' is a Nordic country.
print(f'Estonia is a Nordic country: {'Estonia' in nordic_countries}')
#
#    b. Check if 'Iceland' is a Nordic country. Print 'Iceland is a Nordic country'.
print(f'Iceland is a Nordic country: {'Iceland' in nordic_countries}')
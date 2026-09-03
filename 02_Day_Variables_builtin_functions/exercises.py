from math import pi

# Day 2: 30 Days of python programming

first_name = "Daniela"
last_name = "Collaguazo"
full_name = first_name + " " + last_name
country = "Ecuador"
city = "Quito"
age = 26
year = 2026
is_married = False
is_true = True
is_light_on = False
is_student = True
is_teacher = False
house_number, street, city, county, state, zip_code, email = "7180" , "Brick Kiln Cr", "Beltsville", "Prince George's County" ,"Maryland", "20705", "d.collaguazo@gmail.com"


# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(is_student))
print(type(is_teacher))

print (len(first_name) == len(last_name))


num_one = 5
num_two = 4
total = num_one + num_two
difference = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total)
print(difference)
print(product)
print(division)


radius = 10
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

input_radius = int(input("Enter the radius of the circle: "))
area_of_circle = pi * input_radius ** 2
circum_of_circle = 2 * pi * input_radius

print("Area of the circle: ", area_of_circle)
print("Circumference of the circle: ", circum_of_circle)


input_first_name = input("Enter your first name: ")
input_last_name = input("Enter your last name: ")
input_full_name = input_first_name + " " + input_last_name
print(input_full_name)

help('keywords')

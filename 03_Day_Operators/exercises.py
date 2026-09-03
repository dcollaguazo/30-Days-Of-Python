from math import pi

# Day 3: 30 Days of python programming

# my_age = 42
# height = 1.59
# complex_number = 1 + 1j

# input_base = int(input("Enter the base of the triangle: "))
# input_height = int(input("Enter the height of the triangle: "))
# area_of_triangle = 0.5 * input_base * input_height
# print("The area of the triangle is: ", area_of_triangle)

# input_side_a = int(input("Enter the length of side a: "))   
# input_side_b = int(input("Enter the length of side b: "))
# input_side_c = int(input("Enter the length of side c: "))
# print("The perimeter of the triangle is: ", input_side_a + input_side_b + input_side_c)

# input_length = int(input("Enter the length of the rectangle: "))
# input_width = int(input("Enter the width of the rectangle: "))
# print("The area of the rectangle is: ", input_length * input_width)
# print("The perimeter of the rectangle is: ", 2 * (input_length + input_width))

# input_radius = int(input("Enter the radius of the circle: "))
# area_of_circle = pi * input_radius ** 2
# circum_of_circle = 2 * pi * input_radius
# print("The area of the circle is: ", area_of_circle)
# print("The circumference of the circle is: ", circum_of_circle)

# # Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope = 2
# x_intercept = -2 / 2
# y_intercept = -2
# print("The slope of the line is: ", slope)
# print("The x-intercept of the line is: ", x_intercept)
# print("The y-intercept of the line is: ", y_intercept)

# # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# m = (10 - 2) / (6 - 2)
# euclidean_distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
# print("The slope of the line is: ", m)
# print("The Euclidean distance between the two points is: ", euclidean_distance)

# # Compare the slope and Euclidean distance with the slope and distance you calculated manually.
# print("Comparing slopes", m == slope)

# # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# x = 0
# y = x ** 2 + 6 * x + 9
# print("The value of y is: ", y)

# # Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# len_python = len('python')
# len_dragon = len('dragon')

# print("The length of 'python' compared to 'dragon' is: ", len_python == len_dragon)

# # Use and operator to check if 'on' is found in both 'python' and 'dragon'
# print("Is 'on' found in both  'python' and 'dragon'? ", 'on' in 'python' and 'on' in 'dragon')

# # I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# print("is 'jargon' found in this sentence?", "jargon" in "I hope this course is not full of jargon")

# # There is no 'on' in both dragon and python
# # Find the length of the text python and convert the value to float and convert it to string
# len_python = len('python')
# float_python = float(len_python)


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# x = int(input("Enter a number: "))
# divisible_by_2 = x % 2 == 0
# print("Is the number divisible by 2? ", divisible_by_2)

# # Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# floor_division = 7 // 3
# int_converted = int(2.7)
# print("Is the floor division of 7 by 3 equal to the int converted value of 2.7? ", floor_division == int_converted)

# # Check if type of '10' is equal to type of 10
# type_10_string = type('10')
# type_10_int = type(10)
# print("Is the type of '10' equal to the type of 10? ", type_10_string == type_10_int)

# # Check if int('9.8') is equal to 10
# int_9_8 = int(float('9.8'))
# print("Is int('9.8') equal to 10? ", int_9_8 == 10)

# # Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# hours = int(input("Enter the number of hours worked: "))
# rate_per_hour = int(input("Enter the rate per hour: "))
# pay = hours * rate_per_hour
# print("The pay of the person is: ", pay)


# # Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. 
# # Assume a person can live hundred years
# years = int(input("Enter the number of years: "))
# seconds = years * 365 * 24 * 60 * 60
# print("The number of seconds a person can live is: ", seconds)

for i in range(1,6):
    print(i, 1, i * 1, i ** 2, i ** 3)
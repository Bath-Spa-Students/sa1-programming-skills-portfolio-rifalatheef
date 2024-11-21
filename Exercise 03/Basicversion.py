"""In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information"""

# Make a dictionary
person_info = {
    "name" : "Rifa" ,
    "hometown" : "Kerala" ,
    "age" : 20
}

# print the values on separate lines
print(f"Name: {person_info[' name']}")
print(f"Hometown: {person_info['hometown']}")
print(f"Age : {person_info['age']}")

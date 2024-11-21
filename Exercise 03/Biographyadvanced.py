"""Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?"""

#Ask the user for input
name = input("Enter your full name:")
hometown = input("Enter your hometown:")

#using the while loop 
while True:
    try:
        age= int(input("Enter your age:"))  #
        break  #
    except ValueError:
        print("please enter a valid number for age.")

#creating a dictionary
personal_info = {
    "name" : name,
    "hometown": hometown,
    "age" : age
}

#printing the dictionary
print(f"\nName: {personal_info['name']}")
print(f"Hometown: {personal_info['hometown']}")
print(f"Age: {personal_info['age']}")
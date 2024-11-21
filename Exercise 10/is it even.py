"""Write a program that tests if a value is even or odd. Follow the instructions
outlined below:
Instructions:
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function."""


# Function that confirms if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # Request the user to input a number
    number = int(input("Enter a number: "))
    
    # convey the number to the function and publish the result
    result = check_even_or_odd(number)
    print(result)

# request0 the main function
if __name__:
    main()
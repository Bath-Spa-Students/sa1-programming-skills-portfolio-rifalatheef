"""Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the

3

password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered.
Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted."""

# make it correct
correct_password = "12345"
# write the maximum number 
max_attempts = 5
# analyze the counter 
attempts = 0

# loop until the id enters the correct password or reaches the maximum attempt
while attempts < max_attempts:
    # ask the  id to the password
    password = input("Please enter the password: ")
    
    #Recheck wheather you write the correct password
    if password == correct_password:
        print("Access granted!")
        break
    else:
        #short the seek
        attempts += 1
        remaining_attempts = max_attempts - attempts
        # Brief the id of the incorrect password and remaining attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        
        # If it is reaches the  maximum attempt ,update it
        if attempts == max_attempts:
            print("Maximum attempts reached. The authorities have been alerted.")
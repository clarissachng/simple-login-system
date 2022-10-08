# Login System: Input name and username

# Prompts the user to input their first and last name
firstName = str(input("First Name: ")) 
lastName = str(input('Last Name: '))

# After printing out the user's name, further prompt them to input their username
print("\nHi", firstName, lastName)
print("Please input your username :)\n")

# Stores the username under a variable
username = str(input("Username: "))
print("Your username is", username)

# Password1: Password Maker

# Prompts user to input their password with the reminder that it has to be 12 characters long
print("Please input your password\n") 
print("**Password must be at least 12 characters long**\n" )

# For checking whether the password has more than 12 characters
while True: 
    # We ask the user to input the password
   password = input("Password: ")
   
    # Check if the user has input a password with more than 12 characters
    # If not, the user will be prompt to input the password once again
   if len(password) < 12:
       print("Your password must be longer than 12 characters :(")
       print("Please enter your password again\n")
       continue
    # Otherwise, we believe that the password has more than 12 characters and break the loop.
   else:
       print("\nPassword Accepted!") 
       break

# Password2: Password Checker

# Prompts the user to re-input the password once again for checking
print("Please re-enter your password\n")

while True: 
   # We ask the user to re-input the password once again
   password2 = input("Re-enter password: ")
    
   # Check if both passwords are the same
   # If not, the user will be prompt to input the password once again until both passwords are the same
   if password != password2:
       print("The passwords don't match up :(")
       print("Please reenter the password once again\n")
       continue
   # Otherwise, we believe the condition of both passwords are the same and break the loop.
   else:
       print("\nPassword Accepted!")
       break
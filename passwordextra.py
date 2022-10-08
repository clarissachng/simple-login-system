#password1: input password extra (with lower and uppercase)

print("Please input your password\n" + "**Password must be at least 12 characters long with one uppercase and lowercase letter**\n" )

while True: 
    password = input("Password: ")

    if len(password) < 12:
        print("Your password must be longer than 12 characters :(\n")
        continue
    elif password.upper() == password or password.lower() == password:
        print("Your password must contain at least one lowercase and uppercase letter\n")
        continue
    else:
        print("\nPassword Accepted!")
        break
print("Welcome\n1. Signin\n2. Signup")
response = str(input(""))
if response == "1" or response == "signin":
    username = str(input("Enter your username\n"))
    password = str(input("Enter your password\n"))
elif response == "2" or response == "signup":
    username = str(input("Enter your username\n")).lower()
    email = str(input("Enter your email\n"))
    for char in email:
        if char == "@":
            continue
        else:
            break
    print("That email is not valid, please try again")
    password1 = str(input("Enter your password\n"))
    if len(password1) >= 8 :
        password2 = str(input("Confirm password\n"))
        if password1 == password2:
            print("Password matched\nSignup successful")
        else:
            print("Password not matched\nSignup failed")
    else:
        print("Password too weak")
else:
    print("Invalid request")
            

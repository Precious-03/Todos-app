password = input("Enter a password: ")

if len(password) > 7:
    print("Strong Password")
elif len(password) < 7:
    print("weak password")
else:
    print("Password is OK, but not too strong")

import re

pattern = re.compile(r'')
while True:
    password = input("Please input your password: ")
    if len(password) < 6:
        print("password length must be greater than 6")
    elif re.search(r"[@%!?#$*]", password) is None:
        print("Password must contain at least one special character")
    elif re.search(r"[A-Z]", password) is None:
        print("Password must contain at least one capital letter")
    elif re.search(r"\d", password) is None:
        print("Password must contain at least one digit")
    elif re.match(r"[a-z @!$&*#? 0-9 A-Z]{6}", password):
        pattern = re.compile(r"[0-9 #@!$%&? a-z A-Z]{6}")
        result = pattern.match(password)
        print("password is correct")
        break
    else:
        print("Password doesn't match")

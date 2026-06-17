# Password Strength Checker with Common Password Detection

password = input("Enter your password: ")

# List of common weak passwords
common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "abc123",
    "111111",
    "123123",
    "welcome"
]

# Check if password is common
if password.lower() in common_passwords:
    print("❌ Weak Password")
    print("⚠️ This password is very common and unsafe!")

else:

    length = len(password)

    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    symbols = "!@#$%^&*()_+-="

    # Check each character
    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_number = True

        elif char in symbols:
            has_symbol = True

    # Password strength logic
    if length >= 8 and has_upper and has_lower and has_number and has_symbol:
        print("✅ Strong Password")

    elif length >= 6 and (has_upper or has_number):
        print("⚠️ Medium Password")

    else:
        print("❌ Weak Password")
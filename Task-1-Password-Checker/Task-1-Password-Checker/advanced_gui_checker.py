import tkinter as tk
from tkinter import messagebox

# Function to check password strength
def check_password():

    password = password_entry.get()

    # Common weak passwords
    common_passwords = [
        "123456",
        "password",
        "admin",
        "qwerty",
        "abc123",
        "111111",
        "welcome"
    ]

    # Symbols list
    symbols = "!@#$%^&*()_+-="

    # Common password detection
    if password.lower() in common_passwords:
        result_label.config(
            text="❌ Weak Password\nCommon password detected!",
            fg="red"
        )
        return

    length = len(password)

    has_upper = False
    has_lower = False
    has_number = False
    has_symbol = False

    # Check characters
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

        result_label.config(
            text="✅ Strong Password",
            fg="green"
        )

    elif length >= 6 and (has_upper or has_number):

        result_label.config(
            text="⚠️ Medium Password",
            fg="orange"
        )

    else:

        result_label.config(
            text="❌ Weak Password",
            fg="red"
        )


# Main Window
root = tk.Tk()

root.title("Password Strength Checker")
root.geometry("450x300")
root.config(bg="#1e1e1e")

# Title
title_label = tk.Label(
    root,
    text="🔐 Password Strength Checker",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title_label.pack(pady=20)

# Password Entry
password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14),
    show="*"
)

password_entry.pack(pady=10)

# Check Button
check_button = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=check_password
)

check_button.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e1e"
)

result_label.pack(pady=20)

# Run App
root.mainloop()
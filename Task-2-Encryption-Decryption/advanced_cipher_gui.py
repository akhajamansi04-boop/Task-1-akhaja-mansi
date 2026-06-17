import tkinter as tk
from tkinter import messagebox

# Encryption Function
def encrypt():

    message = message_entry.get("1.0", tk.END).strip()

    try:
        shift = int(shift_entry.get())
    except:
        messagebox.showerror("Error", "Shift key must be a number")
        return

    encrypted_text = ""

    for char in message:

        if char.isalpha():

            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)

            encrypted_text += encrypted_char

        else:
            encrypted_text += char

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, encrypted_text)


# Decryption Function
def decrypt():

    message = message_entry.get("1.0", tk.END).strip()

    try:
        shift = int(shift_entry.get())
    except:
        messagebox.showerror("Error", "Shift key must be a number")
        return

    decrypted_text = ""

    for char in message:

        if char.isalpha():

            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)

            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, decrypted_text)


# Main Window
root = tk.Tk()

root.title("Cyber Security Encryption Tool")
root.geometry("700x500")
root.config(bg="black")

# Title
title = tk.Label(
    root,
    text="🔐 Caesar Cipher Encryption Tool",
    font=("Consolas", 22, "bold"),
    bg="black",
    fg="lime"
)

title.pack(pady=20)

# Message Label
msg_label = tk.Label(
    root,
    text="Enter Message:",
    font=("Consolas", 14),
    bg="black",
    fg="white"
)

msg_label.pack()

# Message Input
message_entry = tk.Text(
    root,
    height=5,
    width=60,
    font=("Consolas", 12),
    bg="#111111",
    fg="lime",
    insertbackground="white"
)

message_entry.pack(pady=10)

# Shift Key
shift_label = tk.Label(
    root,
    text="Enter Shift Key:",
    font=("Consolas", 14),
    bg="black",
    fg="white"
)

shift_label.pack()

shift_entry = tk.Entry(
    root,
    font=("Consolas", 14),
    width=10,
    bg="#111111",
    fg="lime",
    insertbackground="white"
)

shift_entry.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

# Encrypt Button
encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    font=("Consolas", 14, "bold"),
    bg="lime",
    fg="black",
    padx=20,
    pady=10,
    command=encrypt
)

encrypt_btn.grid(row=0, column=0, padx=20)

# Decrypt Button
decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    font=("Consolas", 14, "bold"),
    bg="red",
    fg="white",
    padx=20,
    pady=10,
    command=decrypt
)

decrypt_btn.grid(row=0, column=1, padx=20)

# Output Label
output_label = tk.Label(
    root,
    text="Output:",
    font=("Consolas", 14),
    bg="black",
    fg="white"
)

output_label.pack()

# Output Box
output_box = tk.Text(
    root,
    height=5,
    width=60,
    font=("Consolas", 12),
    bg="#111111",
    fg="cyan",
    insertbackground="white"
)

output_box.pack(pady=10)

# Run Application
root.mainloop()
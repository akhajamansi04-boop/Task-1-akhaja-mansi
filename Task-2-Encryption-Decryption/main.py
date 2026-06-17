# Caesar Cipher Encryption & Decryption

message = input("Enter your message: ")
shift = 3

encrypted_text = ""
decrypted_text = ""

# Encryption
for char in message:

    if char.isalpha():

        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)

        else:
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)

        encrypted_text += encrypted_char

    else:
        encrypted_text += char

print("\n🔒 Encrypted Text:", encrypted_text)

# Decryption
for char in encrypted_text:

    if char.isalpha():

        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)

        else:
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)

        decrypted_text += decrypted_char

    else:
        decrypted_text += char

print("🔓 Decrypted Text:", decrypted_text)
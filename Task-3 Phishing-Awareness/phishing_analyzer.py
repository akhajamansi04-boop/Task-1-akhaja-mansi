suspicious_keywords = [
    "urgent",
    "verify",
    "account suspended",
    "click here",
    "winner",
    "free money",
    "claim prize",
    "bank account",
    "password"
]

message = input("Paste email/message:\n")

red_flags = []

for word in suspicious_keywords:
    if word.lower() in message.lower():
        red_flags.append(word)

print("\n----- Analysis Report -----")

if red_flags:
    print("⚠ Potential Phishing Detected")
    print("\nRed Flags Found:")

    for flag in red_flags:
        print("-", flag)

else:
    print("✅ No obvious phishing indicators found")
import tkinter as tk
from tkinter import scrolledtext
import re

# Analyze phishing message
def analyze_message():

    message = input_box.get("1.0", tk.END)

    suspicious_keywords = [
        "urgent",
        "verify",
        "account suspended",
        "click here",
        "free money",
        "claim prize",
        "winner",
        "bank account",
        "password",
        "otp",
        "limited time",
        "reward",
        "congratulations",
        "login now"
    ]

    red_flags = []
    score = 0

    # Keyword detection
    for keyword in suspicious_keywords:
        if keyword.lower() in message.lower():
            red_flags.append(f"Keyword Detected: {keyword}")
            score += 10

    # URL detection
    urls = re.findall(r'https?://\S+|www\.\S+', message)

    if urls:
        score += 20
        red_flags.append("Suspicious URL Found")

    # URL shorteners
    shorteners = [
        "bit.ly",
        "tinyurl",
        "goo.gl",
        "t.co",
        "shorturl"
    ]

    for url in urls:
        for shortener in shorteners:
            if shortener in url:
                score += 15
                red_flags.append("URL Shortener Detected")

    # Risk level
    if score >= 50:
        risk = "🔴 HIGH RISK"
    elif score >= 20:
        risk = "🟠 MEDIUM RISK"
    else:
        risk = "🟢 LOW RISK"

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END,
        f"Risk Score: {score}/100\n\n"
    )

    output_box.insert(tk.END,
        f"Risk Level: {risk}\n\n"
    )

    output_box.insert(tk.END,
        "Red Flags Found:\n"
    )

    if red_flags:
        for flag in red_flags:
            output_box.insert(tk.END, f"• {flag}\n")
    else:
        output_box.insert(
            tk.END,
            "No major phishing indicators found.\n"
        )

    output_box.insert(
        tk.END,
        "\nRecommendation:\n"
    )

    if score >= 50:
        output_box.insert(
            tk.END,
            "Do NOT click links or share information.\n"
        )
    elif score >= 20:
        output_box.insert(
            tk.END,
            "Verify sender before taking action.\n"
        )
    else:
        output_box.insert(
            tk.END,
            "Appears relatively safe.\n"
        )


# Main Window
root = tk.Tk()

root.title("Phishing Awareness Analyzer")
root.geometry("850x650")
root.configure(bg="black")

# Heading
title = tk.Label(
    root,
    text="🛡 Phishing Awareness Analyzer",
    font=("Consolas", 22, "bold"),
    bg="black",
    fg="lime"
)

title.pack(pady=15)

# Input label
input_label = tk.Label(
    root,
    text="Paste Email or Message:",
    font=("Consolas", 12),
    bg="black",
    fg="white"
)

input_label.pack()

# Input box
input_box = scrolledtext.ScrolledText(
    root,
    width=90,
    height=12,
    bg="#111111",
    fg="lime",
    insertbackground="white",
    font=("Consolas", 11)
)

input_box.pack(pady=10)

# Analyze button
analyze_btn = tk.Button(
    root,
    text="Analyze Message",
    font=("Consolas", 12, "bold"),
    bg="lime",
    fg="black",
    command=analyze_message
)

analyze_btn.pack(pady=10)

# Output label
output_label = tk.Label(
    root,
    text="Analysis Report:",
    font=("Consolas", 12),
    bg="black",
    fg="white"
)

output_label.pack()

# Output box
output_box = scrolledtext.ScrolledText(
    root,
    width=90,
    height=15,
    bg="#111111",
    fg="cyan",
    font=("Consolas", 11)
)

output_box.pack(pady=10)

root.mainloop()
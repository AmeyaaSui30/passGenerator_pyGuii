import tkinter as tk
from tkinter import messagebox
import random
import string
# Generate Password Logic
def generate_password():
    length = length_var.get()
    if not str(length).isdigit() or int(length) < 1:
        messagebox.showerror("Error", "Enter a valid password length.")
        return
    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation
    if not characters:
        messagebox.showerror("Error", "Select at least one character type.")
        return
    password = ''.join(random.choice(characters) for _ in range(int(length)))
    result_var.set(password)
# Copy to Clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")
# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.config(padx=20, pady=20)

# Variables
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Widgets
tk.Label(root, text="Password Length:").pack(anchor='w')
tk.Entry(root, textvariable=length_var, width=10).pack(anchor='w')

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=letters_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack(anchor='w')
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=symbols_var).pack(anchor='w')
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)
tk.Entry(root, textvariable=result_var, width=40, font=("Arial", 12), justify="center").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()
# Run the GUI
root.mainloop()

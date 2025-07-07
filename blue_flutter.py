import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if not str(length).isdigit() or int(length) < 1:
        messagebox.showerror("Oops!", "Enter a valid password length.")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Wait!", "Choose at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(int(length)))
    result_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied!", "Password copied to clipboard.")

root = tk.Tk()
root.title("DarkBoy 🔐")
root.geometry("450x500")
root.configure(bg="#23272a")

# inp
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

tk.Label(root, text="DarkBoy - Password Generator", font=("Helvetica", 16, "bold"), bg="#23272a", fg="#00bfff").pack(pady=20)

frame = tk.Frame(root, bg="#23272a")
frame.pack(pady=10)

tk.Label(frame, text="🔢 Length:", font=("Arial", 12), bg="#23272a", fg="#ffffff").grid(row=0, column=0, sticky='w')
tk.Entry(frame, textvariable=length_var, width=5, bg="#2c2f33", fg="#00bfff", insertbackground="#00bfff").grid(row=0, column=1)

tk.Checkbutton(frame, text="Letters", variable=letters_var, bg="#23272a", fg="#ffffff", font=("Arial", 11), selectcolor="#2c2f33", activebackground="#23272a").grid(row=1, column=0, sticky='w')
tk.Checkbutton(frame, text="Numbers", variable=numbers_var, bg="#23272a", fg="#ffffff", font=("Arial", 11), selectcolor="#2c2f33", activebackground="#23272a").grid(row=2, column=0, sticky='w')
tk.Checkbutton(frame, text="Symbols", variable=symbols_var, bg="#23272a", fg="#ffffff", font=("Arial", 11), selectcolor="#2c2f33", activebackground="#23272a").grid(row=3, column=0, sticky='w')

tk.Button(root, text="Generate", command=generate_password, font=("Arial", 12), bg="#00bfff", fg="#23272a", padx=10, pady=5, activebackground="#005f7f").pack(pady=10)

tk.Entry(root, textvariable=result_var, font=("Courier New", 14), width=30, justify="center", bd=2, relief="groove", bg="#2c2f33", fg="#00ff99", insertbackground="#00ff99").pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 11), bg="#2c2f33", fg="#00bfff", activebackground="#005f7f").pack()

tk.Label(root, text="Made with 💻 by AS", font=("Arial", 9), bg="#23272a", fg="#888888").pack(side="bottom", pady=10)

root.mainloop()

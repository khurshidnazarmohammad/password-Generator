from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


class PasswordGenerator:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator 🔐")
        self.root.geometry("500x350")
        self.root.config(bg="#0f172a")

        title = Label(
            root,
            text="Password Generator",
            font=("Arial", 22, "bold"),
            fg="#00ffcc",
            bg="#0f172a"
        )
        title.pack(pady=10)

        self.password_entry = Entry(
            root,
            font=("Arial", 18),
            width=25,
            justify="center"
        )
        self.password_entry.pack(pady=10)

        length_frame = Frame(root, bg="#0f172a")
        length_frame.pack()

        Label(
            length_frame,
            text="Password Length:",
            font=("Arial", 12),
            fg="white",
            bg="#0f172a"
        ).pack(side=LEFT)

        self.length_entry = Entry(length_frame, width=5)
        self.length_entry.insert(0, "12")
        self.length_entry.pack(side=LEFT, padx=5)

        # Options
        self.uppercase_var = IntVar(value=1)
        self.numbers_var = IntVar(value=1)
        self.symbols_var = IntVar(value=1)

        Checkbutton(
            root,
            text="Uppercase Letters",
            variable=self.uppercase_var,
            bg="#0f172a",
            fg="white",
            selectcolor="#1e293b"
        ).pack()

        Checkbutton(
            root,
            text="Numbers",
            variable=self.numbers_var,
            bg="#0f172a",
            fg="white",
            selectcolor="#1e293b"
        ).pack()

        Checkbutton(
            root,
            text="Symbols",
            variable=self.symbols_var,
            bg="#0f172a",
            fg="white",
            selectcolor="#1e293b"
        ).pack()

        Button(
            root,
            text="Generate Password ⚡",
            command=self.generate_password,
            bg="#00ffcc",
            fg="black",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        Button(
            root,
            text="Copy 📋",
            command=self.copy_password,
            bg="#1e293b",
            fg="white"
        ).pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())

            chars = string.ascii_lowercase

            if self.uppercase_var.get():
                chars += string.ascii_uppercase
            if self.numbers_var.get():
                chars += string.digits
            if self.symbols_var.get():
                chars += string.punctuation

            if not chars:
                messagebox.showerror("Error", "No character set selected!")
                return

            password = "".join(random.choice(chars) for _ in range(length))

            self.password_entry.delete(0, END)
            self.password_entry.insert(0, password)

        except ValueError:
            messagebox.showerror("Error", "Length must be a number!")

    def copy_password(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


if __name__ == "__main__":

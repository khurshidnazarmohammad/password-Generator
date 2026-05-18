from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


class PasswordGenerator:

    def init(self, root):
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
        ).

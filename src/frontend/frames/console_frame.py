import tkinter as tk
from tkinter import ttk


class ConsoleFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Console", padx=10, pady=10)
        self.console_text = tk.Text(self, wrap="word", height=10, width=80)
        self.console_text.pack(fill="both", expand=True)

    def log_message(self, message):
        self.console_text.insert(tk.END, f"{message}\n")
        self.console_text.see(tk.END)

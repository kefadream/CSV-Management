import tkinter as tk
from tkinter import ttk


class ProgressBarFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.progress = ttk.Progressbar(self, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)
        self.progress["maximum"] = 100
        self.progress["value"] = 0

    def update_progress(self, value):
        self.progress["value"] = value
        self.update_idletasks()

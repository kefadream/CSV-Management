# src/ui/config_window.py
import tkinter as tk
from tkinter import filedialog, messagebox
from config import CONFIG, logger
import json


class ConfigWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Configuration")

        self.output_directory = tk.StringVar(value=CONFIG['output_directory'])
        self.default_file_name = tk.StringVar(value=CONFIG['default_file_name'])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Output Directory").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.output_directory, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_output_directory).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.root, text="Default File Name").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.default_file_name, width=50).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Save", command=self.save_config).grid(row=2, column=0, columnspan=3, pady=5)

    def browse_output_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_directory.set(directory)

    def save_config(self):
        CONFIG['output_directory'] = self.output_directory.get()
        CONFIG['default_file_name'] = self.default_file_name.get()
        with open('config.json', 'w') as f:
            json.dump(CONFIG, f, indent=4)
        messagebox.showinfo("Configuration Saved", "Configuration has been saved successfully.")
        logger.info("Configuration saved")

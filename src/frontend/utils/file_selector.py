import pandas as pd
from tkinter import filedialog
import tkinter as tk


class FileSelector:
    def __init__(self, logger):
        self.files = []
        self.logger = logger

    def select_files(self):
        root = tk.Tk()
        root.withdraw()  # Cacher la fenêtre principale
        self.files = filedialog.askopenfilenames(title="Select CSV Files", filetypes=[("CSV Files", "*.csv")])
        if self.files:
            self.logger.info(f"Selected files: {self.files}")
        return self.files

    def read_files(self):
        dataframes = []
        for file_path in self.files:
            df = self.read_file(file_path)
            if df is not None:
                dataframes.append(df)
        return dataframes

    def read_file(self, file_path):
        try:
            df = pd.read_csv(file_path)
            self.logger.info(f"Read file: {file_path}")
            return df
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return None

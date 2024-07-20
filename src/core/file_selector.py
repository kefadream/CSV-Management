import pandas as pd
from tkinter import filedialog
import tkinter as tk
from config import logger


class FileSelector:
    def __init__(self):
        self.files = []

    def select_files(self):
        root = tk.Tk()
        root.withdraw()  # Cacher la fenêtre principale
        self.files = filedialog.askopenfilenames(title="Select CSV Files", filetypes=[("CSV Files", "*.csv")])
        if self.files:
            logger.info(f"Selected files: {self.files}")
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
            logger.info(f"Read file: {file_path}")
            return df
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return None

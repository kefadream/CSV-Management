import pandas as pd
from tkinter import filedialog, messagebox, simpledialog
import json
import os
import tkinter as tk
from config import CONFIG, logger
from src.core import CSVProcessor, DataManager, DataStorage, ColumnSelector
from src.exporters import CSVtoJSONExporter, CSVtoTextExporter, CSVtoCSVExporter
from src.ui.widgets import ActionsFrame, DataManagementFrame, ExportOptionsFrame, ConsoleFrame, ProgressBarFrame
from src.ui.dialogs import show_column_selection_dialog, TextInputDialog, show_rename_columns_dialog
from src.ui.images import load_all_images


class CSVApp:
    def __init__(self, root):
        self.root = root

        # Charger les images
        self.image_loader = load_all_images()

        # Paramètres de configuration
        self.output_directory = tk.StringVar(value=CONFIG['output_directory'])
        self.default_file_name = tk.StringVar(value=CONFIG['default_file_name'])

        # Liste des fichiers sélectionnés
        self.files = []
        self.dataframe = None

        # Widgets de l'interface
        self.create_widgets()

    def create_widgets(self):
        # Cadre principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Utiliser grid pour le placement
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Cadre des actions
        action_frame = ActionsFrame(main_frame, self.image_loader.get_image("select"), self.image_loader.get_image("process"), self.select_files, self.process_csv_files)
        action_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Cadre pour les options de gestion des données
        manage_frame = DataManagementFrame(main_frame, self.image_loader.get_image("delete"), self.image_loader.get_image("filter"), self.image_loader.get_image("edit"),
                                           self.image_loader.get_image("check_duplicates"), self.image_loader.get_image("sort"), self.image_loader.get_image("rename"),
                                           self.remove_columns, self.filter_data, self.edit_data,
                                           self.check_duplicates, self.sort_data, self.rename_columns)
        manage_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        # Cadre pour afficher les informations sur les fichiers CSV
        self.info_frame = tk.LabelFrame(main_frame, text="CSV Information", padx=10, pady=10)
        self.info_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.info_text = tk.Text(self.info_frame, wrap="word", height=20, width=80)
        self.info_text.pack(fill="both", expand=True)

        # Cadre pour les options d'exportation
        export_frame = ExportOptionsFrame(main_frame, self.export_to_csv, self.export_to_json, self.export_to_text)
        export_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        # Cadre pour la console de journalisation
        self.console_frame = ConsoleFrame(main_frame)
        self.console_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # Barre de progression
        self.progress_frame = ProgressBarFrame(main_frame)
        self.progress_frame.grid(row=4, column=0, columnspan=2, pady=10)

    def log_message(self, message):
        self.console_frame.log_message(message)

    def browse_output_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_directory.set(directory)
            self.log_message(f"Output directory set to: {directory}")

    def save_config(self):
        CONFIG['output_directory'] = self.output_directory.get()
        CONFIG['default_file_name'] = self.default_file_name.get()
        with open('config.json', 'w') as f:
            json.dump(CONFIG, f, indent=4)
        messagebox.showinfo("Configuration Saved", "Configuration has been saved successfully.")
        self.log_message("Configuration saved successfully.")

    def select_files(self):
        self.files = filedialog.askopenfilenames(title="Select CSV Files", filetypes=[("CSV Files", "*.csv")])
        if self.files:
            self.log_message(f"Selected {len(self.files)} files: {', '.join(os.path.basename(file) for file in self.files)}")

    def display_csv_info(self, info):
        self.info_text.delete("1.0", tk.END)
        self.info_text.insert(tk.END, info)

    def update_progress(self, value):
        self.progress_frame.update_progress(value)

    def process_csv_files(self):
        if not self.files:
            logger.error("No CSV files selected")
            messagebox.showerror("Error", "No CSV files selected or unable to read files.")
            self.log_message("Error: No CSV files selected or unable to read files.")
            return

        self.update_progress(10)
        self.log_message("Processing selected CSV files...")

        processor = CSVProcessor()
        csv_info = processor.extract_csv_info(self.files)
        self.display_csv_info(csv_info)
        self.log_message("CSV information extracted.")

        self.update_progress(30)

        dataframes = processor.read_files(self.files)
        if not dataframes:
            logger.error("No dataframes to process")
            messagebox.showerror("Error", "Unable to read the selected CSV files.")
            self.log_message("Error: Unable to read the selected CSV files.")
            self.update_progress(0)
            return

        self.update_progress(50)

        column_selector = ColumnSelector()
        selected_columns = column_selector.select_columns(dataframes)
        filtered_dataframes = column_selector.filter_columns(dataframes, selected_columns)

        self.update_progress(70)

        manager = DataManager(pd.concat(filtered_dataframes))
        self.dataframe = manager.dataframe
        self.dataframe, _ = manager.check_and_remove_duplicates()
        self.log_message("Duplicates checked and removed if found.")

        data_storage = DataStorage()
        data_storage.store_data(self.dataframe, self.default_file_name.get())
        messagebox.showinfo("Success", "CSV files processed and merged successfully.")
        self.log_message("CSV files processed and merged successfully.")

        self.update_progress(100)
        self.update_progress(0)

    def export_to_json(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to export.")
            self.log_message("Error: No data available to export.")
            return

        output_file = filedialog.asksaveasfilename(initialdir=self.output_directory.get(), defaultextension=".json",
                                                   filetypes=[("JSON files", "*.json")])
        if output_file:
            exporter = CSVtoJSONExporter(self.dataframe)
            success, message = exporter.export(output_file)
            if success:
                messagebox.showinfo("Success", message)
                self.log_message(message)
            else:
                messagebox.showerror("Error", message)
                self.log_message(f"Error: {message}")

    def export_to_text(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to export.")
            self.log_message("Error: No data available to export.")
            return

        output_file = filedialog.asksaveasfilename(initialdir=self.output_directory.get(), defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt")])
        if output_file:
            exporter = CSVtoTextExporter(self.dataframe)
            success, message = exporter.export(output_file)
            if success:
                messagebox.showinfo("Success", message)
                self.log_message(message)
            else:
                messagebox.showerror("Error", message)
                self.log_message(f"Error: {message}")

    def export_to_csv(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to export.")
            self.log_message("Error: No data available to export.")
            return

        output_file = filedialog.asksaveasfilename(initialdir=self.output_directory.get(), defaultextension=".csv",
                                                   filetypes=[("CSV files", "*.csv")])
        if output_file:
            exporter = CSVtoCSVExporter(self.dataframe)
            success, message = exporter.export(output_file)
            if success:
                messagebox.showinfo("Success", message)
                self.log_message(message)
            else:
                messagebox.showerror("Error", message)
                self.log_message(f"Error: {message}")

    def remove_columns(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to modify.")
            self.log_message("Error: No data available to modify.")
            return

        columns = list(self.dataframe.columns)
        selected_columns = show_column_selection_dialog(self.root, columns)
        if selected_columns:
            manager = DataManager(self.dataframe)
            self.dataframe = manager.remove_columns(selected_columns)
            self.display_csv_info(self.dataframe.to_string())
            messagebox.showinfo("Success", f"Columns {', '.join(selected_columns)} removed successfully.")
            self.log_message(f"Columns {', '.join(selected_columns)} removed successfully.")

    def filter_data(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to filter.")
            self.log_message("Error: No data available to filter.")
            return

        column = TextInputDialog(self.root, "Filter Data", "Enter column name to filter by:").user_input
        if column not in self.dataframe.columns:
            messagebox.showerror("Error", f"Invalid column name: {column}")
            self.log_message(f"Error: Invalid column name: {column}")
            return

        value = TextInputDialog(self.root, "Filter Data", f"Enter value to filter {column} by:").user_input
        if column and value:
            manager = DataManager(self.dataframe)
            self.dataframe = manager.filter_data(column, value)
            self.display_csv_info(self.dataframe.to_string())
            messagebox.showinfo("Success", f"Data filtered by {column} = {value}.")
            self.log_message(f"Data filtered by {column} = {value}.")

    def edit_data(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to edit.")
            self.log_message("Error: No data available to edit.")
            return

        row = simpledialog.askinteger("Edit Data", "Enter row index to edit:")
        column = TextInputDialog(self.root, "Edit Data", "Enter column name to edit:").user_input
        if column not in self.dataframe.columns:
            messagebox.showerror("Error", f"Invalid column name: {column}")
            self.log_message(f"Error: Invalid column name: {column}")
            return

        new_value = TextInputDialog(self.root, "Edit Data", "Enter new value:").user_input
        if row is not None and column and new_value:
            manager = DataManager(self.dataframe)
            self.dataframe = manager.edit_cell(row, column, new_value)
            self.display_csv_info(self.dataframe.to_string())
            messagebox.showinfo("Success", f"Cell at row {row}, column {column} updated to {new_value}.")
            self.log_message(f"Cell at row {row}, column {column} updated to {new_value}.")

    def check_duplicates(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to check.")
            self.log_message("Error: No data available to check.")
            return

        manager = DataManager(self.dataframe)
        duplicates, found = manager.check_and_remove_duplicates()
        if not found:
            messagebox.showinfo("Check Duplicates", "No duplicates found.")
            self.log_message("No duplicates found.")
        else:
            self.display_csv_info(duplicates.to_string())
            if messagebox.askyesno("Duplicates Found", "Duplicates found. Do you want to remove them?"):
                self.dataframe = manager.remove_duplicates()
                self.display_csv_info(self.dataframe.to_string())
                messagebox.showinfo("Success", "Duplicates removed successfully.")
                self.log_message("Duplicates removed successfully.")


    def sort_data(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to sort.")
            self.log_message("Error: No data available to sort.")
            return

        column = TextInputDialog(self.root, "Sort Data", "Enter column name to sort by:").user_input
        if column and column in self.dataframe.columns:
            self.dataframe = self.dataframe.sort_values(by=column)
            self.display_csv_info(self.dataframe.to_string())
            messagebox.showinfo("Success", f"Data sorted by {column}.")
            self.log_message(f"Data sorted by {column}.")
        else:
            messagebox.showerror("Error", f"Invalid column name: {column}.")
            self.log_message(f"Error: Invalid column name: {column}.")

    def rename_columns(self):
        if self.dataframe is None:
            messagebox.showerror("Error", "No data available to modify.")
            self.log_message("Error: No data available to modify.")
            return

        columns = list(self.dataframe.columns)
        columns_map = show_rename_columns_dialog(self.root, columns)
        if columns_map:
            manager = DataManager(self.dataframe)
            self.dataframe = manager.rename_columns(columns_map)
            self.display_csv_info(self.dataframe.to_string())
            messagebox.showinfo("Success", "Columns renamed successfully.")
            self.log_message(f"Columns renamed successfully: {columns_map}")

# Exemple d'utilisation
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVApp(root)
    root.mainloop()
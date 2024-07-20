import tkinter as tk
from tkinter import ttk
from src.ui.tooltips import Tooltip


class ActionsFrame(tk.LabelFrame):
    def __init__(self, parent, select_icon, process_icon, select_files_callback, process_files_callback):
        super().__init__(parent, text="Actions", padx=10, pady=10)
        select_button = tk.Button(self, image=select_icon, command=select_files_callback)
        select_button.pack(side="left", padx=5, pady=5)
        Tooltip(select_button, "Select CSV Files")

        process_button = tk.Button(self, image=process_icon, command=process_files_callback)
        process_button.pack(side="left", padx=5, pady=5)
        Tooltip(process_button, "Process CSV Files")


class DataManagementFrame(tk.LabelFrame):
    def __init__(self, parent, delete_icon, filter_icon, edit_icon, check_duplicates_icon, sort_icon,
                 rename_icon, remove_columns_callback, filter_data_callback, edit_data_callback,
                 check_duplicates_callback, sort_data_callback, rename_columns_callback):
        super().__init__(parent, text="Data Management Options", padx=10, pady=10)

        delete_button = tk.Button(self, image=delete_icon, command=remove_columns_callback)
        delete_button.pack(side="left", padx=5, pady=5)
        Tooltip(delete_button, "Remove Columns")

        filter_button = tk.Button(self, image=filter_icon, command=filter_data_callback)
        filter_button.pack(side="left", padx=5, pady=5)
        Tooltip(filter_button, "Filter Data")

        edit_button = tk.Button(self, image=edit_icon, command=edit_data_callback)
        edit_button.pack(side="left", padx=5, pady=5)
        Tooltip(edit_button, "Edit Data")

        check_duplicates_button = tk.Button(self, image=check_duplicates_icon, command=check_duplicates_callback)
        check_duplicates_button.pack(side="left", padx=5, pady=5)
        Tooltip(check_duplicates_button, "Check Duplicates")

        sort_button = tk.Button(self, image=sort_icon, command=sort_data_callback)
        sort_button.pack(side="left", padx=5, pady=5)
        Tooltip(sort_button, "Sort Data")

        rename_button = tk.Button(self, image=rename_icon, command=rename_columns_callback)
        rename_button.pack(side="left", padx=5, pady=5)
        Tooltip(rename_button, "Rename Columns")


class ExportOptionsFrame(tk.LabelFrame):
    def __init__(self, parent, export_csv_callback, export_json_callback, export_text_callback):
        super().__init__(parent, text="Export Options", padx=10, pady=10)

        export_csv_button = tk.Button(self, text="Export to CSV", command=export_csv_callback)
        export_csv_button.pack(side="left", padx=5, pady=5)
        Tooltip(export_csv_button, "Export to CSV")

        export_json_button = tk.Button(self, text="Export to JSON", command=export_json_callback)
        export_json_button.pack(side="left", padx=5, pady=5)
        Tooltip(export_json_button, "Export to JSON")

        export_text_button = tk.Button(self, text="Export to Text", command=export_text_callback)
        export_text_button.pack(side="left", padx=5, pady=5)
        Tooltip(export_text_button, "Export to Text")


class ConsoleFrame(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Console", padx=10, pady=10)
        self.console_text = tk.Text(self, wrap="word", height=10, width=80)
        self.console_text.pack(fill="both", expand=True)

    def log_message(self, message):
        self.console_text.insert(tk.END, f"{message}\n")
        self.console_text.see(tk.END)


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

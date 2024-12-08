import tkinter as tk
from ..utils import Tooltip


class DataManagementFrame(tk.LabelFrame):
    def __init__(self, parent, delete_icon, filter_icon, edit_icon, check_duplicates_icon, sort_icon,
                 rename_icon, remove_duplicates, remove_columns_callback, filter_data_callback, edit_data_callback,
                 check_duplicates_callback, sort_data_callback, rename_columns_callback, impute_data_callback):
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

        impute_button = tk.Button(self, image=remove_duplicates, command=impute_data_callback)
        impute_button.pack(side="left", padx=5, pady=5)
        Tooltip(impute_button, "Impute data")



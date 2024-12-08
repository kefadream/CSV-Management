import tkinter as tk
from ..utils import Tooltip


class ActionsFrame(tk.LabelFrame):
    def __init__(self, parent, select_icon, process_icon, select_files_callback, process_files_callback):
        super().__init__(parent, text="Actions", padx=10, pady=10)
        select_button = tk.Button(self, image=select_icon, command=select_files_callback)
        select_button.pack(side="left", padx=5, pady=5)
        Tooltip(select_button, "Select CSV Files")

        process_button = tk.Button(self, image=process_icon, command=process_files_callback)
        process_button.pack(side="left", padx=5, pady=5)
        Tooltip(process_button, "Process CSV Files")

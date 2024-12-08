import tkinter as tk
from ..utils import Tooltip


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



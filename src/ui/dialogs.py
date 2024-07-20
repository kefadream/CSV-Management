import tkinter as tk
from tkinter import simpledialog


class TextInputDialog(simpledialog.Dialog):
    def __init__(self, parent, title, prompt):
        self.prompt = prompt
        self.user_input = None
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text=self.prompt).grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=1)
        return self.entry

    def apply(self):
        self.user_input = self.entry.get()


def show_column_selection_dialog(parent, columns):
    dialog = tk.Toplevel(parent)
    dialog.title("Select Columns to Remove")

    selected_columns = []

    for column in columns:
        var = tk.BooleanVar(value=False)
        chk = tk.Checkbutton(dialog, text=column, variable=var)
        chk.pack(anchor="w")
        selected_columns.append((column, var))

    def on_ok():
        nonlocal selected_columns
        selected_columns = [col for col, var in selected_columns if var.get()]
        dialog.destroy()

    ok_button = tk.Button(dialog, text="OK", command=on_ok)
    ok_button.pack(pady=10)

    dialog.wait_window(dialog)
    return selected_columns


def show_rename_columns_dialog(parent, columns):
    dialog = tk.Toplevel(parent)
    dialog.title("Rename Columns")

    result = {}  # Initialisation du dictionnaire pour stocker les résultats

    column_vars = []
    new_name_vars = []

    for column in columns:
        column_var = tk.StringVar(value=column)
        new_name_var = tk.StringVar()

        tk.Label(dialog, text=column).pack(anchor="w")
        tk.Entry(dialog, textvariable=new_name_var).pack(anchor="w")

        column_vars.append(column_var)
        new_name_vars.append(new_name_var)

    def on_ok():
        nonlocal result, column_vars, new_name_vars
        result = {column_var.get(): new_name_var.get() for column_var, new_name_var in zip(column_vars, new_name_vars) if new_name_var.get()}
        dialog.destroy()

    ok_button = tk.Button(dialog, text="OK", command=on_ok)
    ok_button.pack(pady=10)

    dialog.wait_window(dialog)
    return result


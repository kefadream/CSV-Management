import tkinter as tk


class ColumnSelectionDialog(tk.Toplevel):
    def __init__(self, parent, columns):
        super().__init__(parent)
        self.title("Select Columns to Remove")
        self.transient(parent)
        self.grab_set()  # Rend la fenêtre modale

        self.selected_columns = []
        self._column_vars = []

        # Création des cases à cocher
        for column in columns:
            var = tk.BooleanVar(value=False)
            chk = tk.Checkbutton(self, text=column, variable=var)
            chk.pack(anchor="w", padx=10, pady=2)
            self._column_vars.append((column, var))

        # Bouton OK
        ok_button = tk.Button(self, text="OK", command=self._on_ok)
        ok_button.pack(pady=10)

    def _on_ok(self):
        self.selected_columns = [col for col, var in self._column_vars if var.get()]
        self.destroy()

    def show(self):
        # Attend la fermeture de la fenêtre
        self.wait_window(self)
        return self.selected_columns

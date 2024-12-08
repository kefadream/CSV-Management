import tkinter as tk


class RenameColumnsDialog(tk.Toplevel):
    def __init__(self, parent, columns):
        super().__init__(parent)
        self.title("Rename Columns")
        self.transient(parent)
        self.grab_set()  # Rend la fenêtre modale

        self.result = {}

        self.column_vars = []
        self.new_name_vars = []

        # Création des champs de saisie pour le nouveau nom
        for column in columns:
            tk.Label(self, text=column).pack(anchor="w", padx=10, pady=2)

            new_name_var = tk.StringVar()
            tk.Entry(self, textvariable=new_name_var).pack(anchor="w", padx=10, pady=2)

            # On stocke la colonne d'origine et la variable associée au nouveau nom
            self.column_vars.append(column)
            self.new_name_vars.append(new_name_var)

        # Bouton OK
        ok_button = tk.Button(self, text="OK", command=self._on_ok)
        ok_button.pack(pady=10)

    def _on_ok(self):
        # On ne garde que les entrées où il y a un nouveau nom
        self.result = {column: var.get() for column, var in zip(self.column_vars, self.new_name_vars) if var.get()}
        self.destroy()

    def show(self):
        # Attend la fermeture de la fenêtre
        self.wait_window(self)
        return self.result


# src/ui/main_window.py
import tkinter as tk
from src.ui.app import CSVApp

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Management Tool")
        self.create_menu()
        self.csv_app = CSVApp(root)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_files)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        config_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Config", menu=config_menu)
        config_menu.add_command(label="Settings", command=self.open_config)

    def open_files(self):
        self.csv_app.select_files()

    def open_config(self):
        from src.ui.config_window import ConfigWindow
        config_window = tk.Toplevel(self.root)
        ConfigWindow(config_window)


if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()

from .utils import read_file, select_columns, filter_columns
from .data_storage import DataStorage

import pandas as pd


class CSVProcessor:
    """
    Classe pour traiter les fichiers CSV.

    Methods:
        extract_csv_info(files): Extrait des informations sur les fichiers CSV.
        read_files(files): Lit les fichiers CSV et retourne une liste de dataframes.
        process_files(files, output_directory, default_file_name): Traite les fichiers CSV, sélectionne les colonnes, fusionne les dataframes et stocke le résultat.
    """
    def extract_csv_info(self, logger, files):
        """
        Extrait des informations sur les fichiers CSV.

        Args:
            files (list): Liste des chemins des fichiers CSV.

        Returns:
            str: Informations sur les fichiers CSV.
        """
        self.logger = logger
        info = ""
        for file in files:
            try:
                df = pd.read_csv(file)
                info += f"File: {file}\n"
                info += f"Columns: {', '.join(df.columns)}\n"
                info += f"Total Records: {len(df)}\n"
                info += f"Data Types:\n{df.dtypes}\n"
                info += f"First 5 Records:\n{df.head()}\n"
                info += f"Last 5 Records:\n{df.tail()}\n"
                info += "-" * 50 + "\n"
            except Exception as e:
                logger.error(f"Error reading file {file}: {e}")
                info += f"Error reading file {file}: {e}\n"
        return info

    def read_files(self, files):
        """
        Lit les fichiers CSV et retourne une liste de dataframes.

        Args:
            files (list): Liste des chemins des fichiers CSV.

        Returns:
            list: Liste des dataframes.
        """
        dataframes = [read_file(fp) for fp in files]
        return dataframes

    def process_files(self, files, default_file_name, data_manager):
        dataframes = self.read_files(files)

        if not dataframes:
            self.logger.error("No dataframes to process")
            return

        selected_columns = select_columns(dataframes)
        filtered_dataframes = filter_columns(dataframes, selected_columns)

        merged_dataframe = data_manager.merge_dataframes(filtered_dataframes)
        if merged_dataframe is not None:
            cleaned_dataframe = data_manager.remove_duplicates(merged_dataframe)

            data_storage = DataStorage()
            data_storage.store_data(cleaned_dataframe, default_file_name)
        else:
            self.logger.error("Merging dataframes failed")

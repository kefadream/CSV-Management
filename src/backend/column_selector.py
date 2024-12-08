# src/core/column_selector.py
from .config import logger


class ColumnSelector:
    """
    Classe pour sélectionner et filtrer les colonnes dans les dataframes.

    Methods:
        select_columns(dataframes): Sélectionne toutes les colonnes uniques des dataframes.
        filter_columns(dataframes, selected_columns): Filtre les dataframes pour ne garder que les colonnes sélectionnées.
    """
    def select_columns(self, dataframes):
        """
        Sélectionne toutes les colonnes uniques des dataframes.

        Args:
            dataframes (list): Liste des dataframes.

        Returns:
            list: Liste des colonnes sélectionnées.
        """
        all_columns = set()
        for df in dataframes:
            all_columns.update(df.columns)

        selected_columns = list(all_columns)  # Pour l'exemple, sélectionnons toutes les colonnes
        logger.info(f"Selected columns: {selected_columns}")
        return selected_columns

    def filter_columns(self, dataframes, selected_columns):
        """
        Filtre les dataframes pour ne garder que les colonnes sélectionnées.

        Args:
            dataframes (list): Liste des dataframes.
            selected_columns (list): Liste des colonnes sélectionnées.

        Returns:
            list: Liste des dataframes filtrés.
        """
        filtered_dfs = []
        for df in dataframes:
            filtered_dfs.append(df[selected_columns])
        logger.info("Filtered dataframes by selected columns")
        return filtered_dfs

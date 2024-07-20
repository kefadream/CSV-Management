import pandas as pd


class DataManager:
    """
    Classe pour gérer les opérations sur les données du dataframe.

    Attributes:
        dataframe (pandas.DataFrame): Le dataframe à gérer.

    Methods:
        remove_columns(columns): Supprime les colonnes spécifiées du dataframe.
        filter_data(column, value): Filtre le dataframe en fonction de la colonne et de la valeur spécifiées.
        edit_cell(row, column, new_value): Modifie une cellule spécifique dans le dataframe.
        check_and_remove_duplicates(): Vérifie et supprime les doublons du dataframe.
        remove_duplicates(): Supprime les doublons du dataframe.
        merge_dataframes(dataframes): Fusionne une liste de dataframes.
    """
    def __init__(self, dataframe):
        """
        Initialise le DataManager avec le dataframe.

        Args:
            dataframe (pandas.DataFrame): Le dataframe à gérer.
        """
        self.dataframe = dataframe

    def remove_columns(self, columns):
        """
        Supprime les colonnes spécifiées du dataframe.

        Args:
            columns (list): Liste des colonnes à supprimer.

        Returns:
            pandas.DataFrame: Le dataframe modifié.
        """
        self.dataframe.drop(columns=columns, inplace=True)
        return self.dataframe

    def rename_columns(self, columns_map):
        """
        Renomme les colonnes spécifiées du dataframe.

        Args:
            columns_map (dict): Dictionnaire avec les colonnes à renommer comme clés et les nouveaux noms comme valeurs.

        Returns:
            pandas.DataFrame: Le dataframe modifié.
        """
        self.dataframe.rename(columns=columns_map, inplace=True)
        return self.dataframe

    def filter_data(self, column, value):
        """
        Filtre le dataframe en fonction de la colonne et de la valeur spécifiées.

        Args:
            column (str): Le nom de la colonne à filtrer.
            value (str): La valeur à filtrer.

        Returns:
            pandas.DataFrame: Le dataframe filtré.
        """
        self.dataframe = self.dataframe[self.dataframe[column] == value]
        return self.dataframe

    def edit_cell(self, row, column, new_value):
        """
        Modifie une cellule spécifique dans le dataframe.

        Args:
            row (int): L'index de la ligne de la cellule.
            column (str): Le nom de la colonne de la cellule.
            new_value (str): La nouvelle valeur à attribuer à la cellule.

        Returns:
            pandas.DataFrame: Le dataframe modifié.
        """
        self.dataframe.at[row, column] = new_value
        return self.dataframe

    def check_and_remove_duplicates(self):
        """
        Vérifie et supprime les doublons du dataframe.

        Returns:
            tuple: Le dataframe sans doublons et un booléen indiquant si des doublons ont été trouvés.
        """
        duplicates = self.dataframe[self.dataframe.duplicated()]
        if not duplicates.empty:
            self.dataframe = self.dataframe.drop_duplicates()
            return self.dataframe, True
        return self.dataframe, False

    def remove_duplicates(self):
        """
        Supprime les doublons du dataframe.

        Returns:
            pandas.DataFrame: Le dataframe sans doublons.
        """
        self.dataframe = self.dataframe.drop_duplicates()
        return self.dataframe

    def merge_dataframes(self, dataframes, logger):
        """
        Fusionne une liste de dataframes.

        Args:
            dataframes (list): Liste des dataframes à fusionner.

        Returns:
            pandas.DataFrame: Le dataframe fusionné.
        """
        try:
            merged_df = pd.concat(dataframes, ignore_index=True)
            return merged_df
        except Exception as e:
            logger.error(f"Error merging dataframes: {e}")
            return None

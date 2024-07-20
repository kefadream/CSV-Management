from config import logger

class CSVtoCSVExporter:
    """
    Classe pour exporter des données de CSV vers CSV.

    Attributes:
        dataframe (pandas.DataFrame): Le dataframe à exporter.

    Methods:
        export(output_file): Exporte le dataframe en fichier CSV.
    """
    def __init__(self, dataframe):
        """
        Initialise le CSVtoCSVExporter avec le dataframe.

        Args:
            dataframe (pandas.DataFrame): Le dataframe à exporter.
        """
        self.dataframe = dataframe

    def export(self, output_file):
        """
        Exporte le dataframe en fichier CSV.

        Args:
            output_file (str): Le chemin du fichier de sortie.

        Returns:
            tuple: Un tuple (bool, str) indiquant le succès ou l'échec de l'exportation.
        """
        try:
            self.dataframe.to_csv(output_file, index=False)
            logger.info(f"Data exported to CSV at {output_file}")
            return True, f"Data exported to CSV at {output_file}"
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            return False, f"Error exporting to CSV: {e}"

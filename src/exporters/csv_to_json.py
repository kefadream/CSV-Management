# src/exporters/csv_to_json.py
from config import logger


class CSVtoJSONExporter:
    """
    Classe pour exporter des données de CSV vers JSON.

    Attributes:
        dataframe (pandas.DataFrame): Le dataframe à exporter.

    Methods:
        export(output_file): Exporte le dataframe en fichier JSON.
    """
    def __init__(self, dataframe):
        """
        Initialise le CSVtoJSONExporter avec le dataframe.

        Args:
            dataframe (pandas.DataFrame): Le dataframe à exporter.
        """
        self.dataframe = dataframe

    def export(self, output_file):
        """
        Exporte le dataframe en fichier JSON.

        Args:
            output_file (str): Le chemin du fichier de sortie.

        Returns:
            tuple: Un tuple (bool, str) indiquant le succès ou l'échec de l'exportation.
        """
        try:
            self.dataframe.to_json(output_file, orient='records', lines=True)
            logger.info(f"Data exported to JSON at {output_file}")
            return True, f"Data exported to JSON at {output_file}"
        except Exception as e:
            logger.error(f"Error exporting to JSON: {e}")
            return False, f"Error exporting to JSON: {e}"

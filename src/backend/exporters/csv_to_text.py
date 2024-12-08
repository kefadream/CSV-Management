# src/exporters/csv_to_txt.py

class CSVtoTextExporter:
    """
    Classe pour exporter des données de CSV vers texte.

    Attributes:
        dataframe (pandas.DataFrame): Le dataframe à exporter.

    Methods:
        export(output_file): Exporte le dataframe en fichier texte.
    """
    def __init__(self, logger, dataframe):
        """
        Initialise le CSVtoTextExporter avec le dataframe.

        Args:
            dataframe (pandas.DataFrame): Le dataframe à exporter.
        """
        self.logger = logger
        self.dataframe = dataframe

    def export(self, output_file):
        """
        Exporte le dataframe en fichier texte.

        Args:
            output_file (str): Le chemin du fichier de sortie.

        Returns:
            tuple: Un tuple (bool, str) indiquant le succès ou l'échec de l'exportation.
        """
        try:
            self.dataframe.to_csv(output_file, index=False, sep='\t')
            self.logger.info(f"Data exported to text at {output_file}")
            return True, f"Data exported to text at {output_file}"
        except Exception as e:
            self.logger.error(f"Error exporting to text: {e}")
            return False, f"Error exporting to text: {e}"
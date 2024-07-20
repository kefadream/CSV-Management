import pandas as pd
import os
from config import logger, CONFIG

class DataStorage:
    def store_data(self, data, file_name=None):
        if file_name is None:
            file_name = CONFIG['default_file_name']
        output_path = os.path.join(CONFIG['output_directory'], file_name)
        try:
            os.makedirs(CONFIG['output_directory'], exist_ok=True)
            data.to_csv(output_path, index=False)
            logger.info(f"Data stored at {output_path}")
        except Exception as e:
            logger.error(f"Error storing data: {e}")

    def load_data(self, file_name):
        try:
            df = pd.read_csv(file_name)
            logger.info(f"Loaded data from {file_name}")
            return df
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return None

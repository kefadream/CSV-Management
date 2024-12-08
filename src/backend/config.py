import json
import logging
import os

# Définir le chemin du fichier de configuration
CONFIG_FILE = 'data/config.json'

# Valeurs par défaut de la configuration
default_config = {
    'output_directory': './output',
    'default_file_name': 'merged_data.csv'
}

# Vérifier si le fichier de configuration existe, sinon le créer avec les valeurs par défaut
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(default_config, f, indent=4)

# Charger la configuration
with open(CONFIG_FILE, 'r') as f:
    CONFIG = json.load(f)

# Configuration du journal
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('data/csv_management.log'), logging.StreamHandler()])

logger = logging.getLogger(__name__)

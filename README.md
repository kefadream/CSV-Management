# Preview
![main_interface2](https://github.com/user-attachments/assets/46c9e3c6-bd6e-46ca-bec7-aeee1208517a)
## Options
![remove_widget](https://github.com/user-attachments/assets/7f0512e2-2b19-4fd3-b35c-5c008c959f75)
![filter_widget](https://github.com/user-attachments/assets/1e1cc07b-0e01-4a28-9144-683255350b9c)
![edit_widget](https://github.com/user-attachments/assets/db7d2ea2-bb6b-4779-8cf2-367581d23282)
![check_duplicate_widget](https://github.com/user-attachments/assets/1ffd680c-6962-481e-8f2e-f41523363ee5)
![sort_data_widget](https://github.com/user-attachments/assets/158e304e-b973-4919-954a-2df562b1c8ec)
![rename_widget](https://github.com/user-attachments/assets/33eac867-b97e-47ce-9892-7123a6b9b1f8)


# CSV Management Tool

## Description

Le CSV Management Tool est une application permettant de lire, traiter, filtrer et exporter des fichiers CSV. L'interface utilisateur permet une gestion facile des fichiers CSV et des opérations sur les données.

## Installation

Clonez ce dépôt et installez les dépendances :

```bash
git clone https://github.com/votre-repo/csv-management-tool.git
cd csv-management-tool
pip install -r requirements.txt
```

## Utilisation
### Interface Utilisateur (UI)
Pour lancer l'interface utilisateur, exécutez le fichier main.py :

```bash
python src/ui/main_window.py
```

## Modules
### src/exporters : 
Contient les classes pour exporter les dataframes en différents formats.

#### CSVtoJSONExporter : 
Exporte le dataframe en JSON.

#### CSVtoTextExporter : 
Exporte le dataframe en texte.

#### CSVtoCSVExporter
Exporte le dataframe en CSV.

### src/core : 
Contient les classes pour gérer les opérations sur les dataframes.

#### CSVProcessor : 
Traite les fichiers CSV.

#### ColumnSelector : 
Sélectionne et filtre les colonnes des dataframes.

#### DataManager : 
Gère les opérations sur les dataframes (suppression de colonnes, filtrage, édition de cellules, vérification et suppression des doublons, fusion des dataframes).

#### DataStorage : 
Stocke et charge les dataframes.

#### FileSelector : 
Sélectionne les fichiers CSV à partir de l'interface utilisateur.

### src/ui : 
Contient les classes pour l'interface utilisateur.

#### CSVApp : 
L'application principale pour gérer les fichiers CSV.

#### ConfigWindow : 
La fenêtre de configuration.

#### Dialogs
Affiche des boîtes de dialogue pour les interactions utilisateur.

#### Tooltip : 
Affiche des infobulles pour les widgets de l'interface.

## Configuration
Les paramètres de configuration sont stockés dans le fichier config.json. Vous pouvez modifier ce fichier pour définir le répertoire de sortie par défaut et le nom de fichier par défaut.

```json
{
    "output_directory": "output",
    "default_file_name": "merged.csv"
}
```

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.


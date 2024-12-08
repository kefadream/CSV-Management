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

The CSV Management Tool is an application that allows you to read, process, filter, and export CSV files. Its user interface enables easy management of CSV files and data operations.


## Installation
Clone this repository and install the dependencies:

```bash
git clone https://github.com/votre-repo/csv-management-tool.git
cd csv-management-tool
pip install -r requirements.txt
```

## Usage
### User Interface (UI)
To launch the user interface, run the main.py file:

```bash
python src/ui/main_window.py
```

## Modules

### src/exporters:
Contains classes for exporting dataframes in various formats.

### CSVtoJSONExporter:
Exports the dataframe to JSON.

### CSVtoTextExporter:
Exports the dataframe to plain text.

### CSVtoCSVExporter:
Exports the dataframe to CSV.

## src/core:
### Contains classes to handle dataframe operations.

- CSVProcessor → Processes CSV files.
- ColumnSelector → Selects and filters columns in dataframes.
- DataManager → Manages dataframe operations (column deletion, filtering, cell editing, duplicate checking and removal, dataframe merging).
- DataStorage → Stores and loads dataframes.
- FileSelector → Selects CSV files from the user interface.

## src/ui:
### Contains classes for the user interface.

- CSVApp → The main application for managing CSV files.
- ConfigWindow → The configuration window.
- Dialogs → Displays dialog boxes for user interactions.
- Tooltip → Displays tooltips for UI widgets.

### Configuration

```json
{
    "output_directory": "output",
    "default_file_name": "merged.csv"
}
```

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

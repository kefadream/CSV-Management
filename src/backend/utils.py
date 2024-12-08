import pandas as pd

def read_file(logger, file_path):
    """
    Lit un fichier CSV et retourne un dataframe.

    Args:
        logger (): fonction de logger
        file_path (str): Le chemin du fichier CSV.

    Returns:
        pandas.DataFrame: Le dataframe lu.
    """


    try:
        df = pd.read_csv(file_path)
        logger.info(f"Read file: {file_path}")
        return df
    except pd.errors.EmptyDataError:
        logger.error(f"File is empty: {file_path}")
    except pd.errors.ParserError:
        logger.error(f"Error parsing file: {file_path}")
    except Exception as e:
        logger.error(f"Unexpected error reading file {file_path}: {e}")
    return None

def select_columns(logger, dataframes):
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
    selected_columns = list(all_columns)
    logger.info(f"Selected columns: {selected_columns}")
    return selected_columns

def filter_columns(logger, dataframes, selected_columns):
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

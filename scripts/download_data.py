import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

def create_project_structure():
    """Crea la estructura básica del proyecto."""
    directories = ['data']

    # Obtener el directorio actual
    current_dir = os.getcwd()

    # Crear las carpetas necesarias
    for directory in directories:
        dir_path = os.path.join(current_dir, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Carpeta creada: {dir_path}")
        else:
            print(f"La carpeta ya existe: {dir_path}")

def setup_kaggle_credentials():
    """Configura las credenciales de Kaggle desde las variables de entorno."""
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)

    kaggle_file = os.path.join(kaggle_dir, "kaggle.json")
    if not os.path.exists(kaggle_file):
        try:
            kaggle_token = {
                "username": os.environ['KAGGLE_USERNAME'],
                "key": os.environ['KAGGLE_KEY']
            }
            with open(kaggle_file, 'w') as f:
                json.dump(kaggle_token, f)
            os.chmod(kaggle_file, 0o600)
            print("Credenciales de Kaggle configuradas correctamente")
        except KeyError as e:
            print(f"Error: No se encontraron las variables de entorno necesarias: {e}")
            raise

def download_dataset():
    """Descarga y descomprime el dataset desde Kaggle."""
    dataset = "blastchar/telco-customer-churn"
    output_dir = os.path.join(os.getcwd(), "data")

    try:
        api = KaggleApi()
        api.authenticate()
        print("Autenticación con Kaggle exitosa")

        print(f"Descargando dataset '{dataset}' en '{output_dir}'...")
        api.dataset_download_files(dataset, path=output_dir, unzip=True)
        print("Dataset descargado y descomprimido exitosamente")

        # Listar archivos descargados
        files = os.listdir(output_dir)
        print("\nArchivos en la carpeta data:")
        for file in files:
            print(f"- {file}")

    except Exception as e:
        print(f"Error al descargar el dataset: {e}")
        raise

def create_initial_notebook():
    """Crea un notebook inicial si no existe."""
    notebook_path = os.path.join(os.getcwd(), "notebooks", "paez_ramirez_jean_carlos_KNN.ipynb")

    if not os.path.exists(notebook_path):
        try:
            import nbformat as nbf

            nb = nbf.v4.new_notebook()

            # Crear celdas iniciales
            cells = [
                nbf.v4.new_markdown_cell(
                    "# Análisis de Datos usando KNN\n\n"
                    "**Autor:** Jean Carlos Páez Ramírez\n\n"
                    "## Objetivo\n"
                    "Implementar el algoritmo K-Nearest Neighbors (KNN) para análisis de datos."
                ),
                nbf.v4.new_code_cell(
                    "# Importar bibliotecas necesarias\n"
                    "import pandas as pd\n"
                    "import numpy as np\n"
                    "import matplotlib.pyplot as plt\n"
                    "import seaborn as sns\n"
                    "from sklearn.neighbors import KNeighborsClassifier\n"
                    "from sklearn.model_selection import train_test_split\n"
                    "from sklearn.preprocessing import StandardScaler"
                )
            ]

            nb['cells'] = cells

            with open(notebook_path, 'w', encoding='utf-8') as f:
                nbf.write(nb, f)

            print(f"Notebook inicial creado en: {notebook_path}")
        except Exception as e:
            print(f"Error al crear el notebook inicial: {e}")

if __name__ == "__main__":
    print("Iniciando configuración del proyecto...")
    create_project_structure()
    setup_kaggle_credentials()
    download_dataset()
    create_initial_notebook()
    print("Configuración del proyecto completada")
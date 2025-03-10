import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

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

    # Crear la carpeta data si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Carpeta creada: {output_dir}")

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

if __name__ == "__main__":
    print("Iniciando descarga del dataset...")
    setup_kaggle_credentials()
    download_dataset()
    print("Proceso completado")
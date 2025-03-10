import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

def setup_kaggle_credentials():
    """Configura las credenciales de Kaggle desde las variables de entorno."""
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)

    kaggle_file = os.path.join(kaggle_dir, "kaggle.json")
    if not os.path.exists(kaggle_file):
        kaggle_token = {
            "username": os.environ['KAGGLE_USERNAME'],
            "key": os.environ['KAGGLE_KEY']
        }
        with open(kaggle_file, 'w') as f:
            json.dump(kaggle_token, f)
        os.chmod(kaggle_file, 0o600)

def download_dataset():
    """Descarga y descomprime el dataset desde Kaggle."""
    dataset = "blastchar/telco-customer-churn"
    output_dir = "data"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=output_dir, unzip=True)
    print(f"Dataset descargado y descomprimido en '{output_dir}'")

if __name__ == "__main__":
    setup_kaggle_credentials()
    download_dataset()
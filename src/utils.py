import os

# Raíz del proyecto (src/..)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(f"proyect root: {PROJECT_ROOT}")
# Carpeta principal de datasets
DATASET_FOLDER = os.path.join(PROJECT_ROOT,"src", "datasets")
print(f"dataset folder: {DATASET_FOLDER}")
EXTRACTED_FOLDER = os.path.join(DATASET_FOLDER, "extracted")


import os
import pandas as pd
from time import sleep
from utils import DATASET_FOLDER


def analyze_xls_file():
    try:
        os.system("clear")
        sleep(1)
        xls_path = os.path.join(DATASET_FOLDER,"PAKDD2010_VariablesList.XLS")
        df = pd.read_excel(xls_path, engine="xlrd")
        return df

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
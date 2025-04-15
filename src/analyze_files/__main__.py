import pandas as pd
import os
from time import sleep
def analyze_xls_file():
    try:
        os.system("clear")
        sleep(1)
        xls_path = os.path.join(os.getcwd(), "datasets/PAKDD2010_VariablesList.XLS")
        df = pd.read_excel(xls_path, engine="xlrd")

        print("Columnas encontradas:")
        print(df.columns)

        print("\nVista previa:")
        print(df.head())

        print("\nInformación general:")
        print(df.info())

        print("\nEstadísticas descriptivas:")
        print(df.describe())

        print("\nValores únicos:")
        print(df.nunique())

        print("\nValores nulos:")
        print(df.isnull().sum())

        print("\nValores duplicados:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def analyze_txt_files():
    txt_folder1 = os.path.join(os.getcwd(), "datasets")
    txt_folder2 = os.path.join(os.getcwd(), "datasets/extracted")
    txt_files1 = [f for f in os.listdir(txt_folder1) if f.endswith(".txt")]
    txt_files2 = [f for f in os.listdir(txt_folder2) if f.endswith(".txt")]
    print(txt_files1)
    print(txt_files2)

if __name__ == "__main__":
    analyze_xls_file()
    sleep(10)
    os.system("clear")
    sleep(1)
    analyze_txt_files()
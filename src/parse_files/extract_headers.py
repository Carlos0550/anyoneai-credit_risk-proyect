import os
from utils import DATASET_FOLDER
import pandas as pd
def get_column_headers_from_xls() -> list:
    xls_path = os.path.join(DATASET_FOLDER,"PAKDD2010_VariablesList.XLS")
    df = pd.read_excel(xls_path, engine="xlrd")
    return df["Var_Title"].dropna().tolist()
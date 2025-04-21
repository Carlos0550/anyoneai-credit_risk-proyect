import os
from .extract_headers import get_column_headers_from_xls
from .txt_reader import read_flexible_txt
from utils import DATASET_FOLDER
def get_txt_files():
    
    txt_folder1 = DATASET_FOLDER
    txt_folder2 = os.path.join(DATASET_FOLDER, "extracted")

    txt_files1 = [
        os.path.join(txt_folder1, f)
        for f in os.listdir(txt_folder1) if f.endswith(".txt")
    ]

    txt_files2 = [
        os.path.join(txt_folder2, f)
        for f in os.listdir(txt_folder2) if f.endswith(".txt")
    ]

    return txt_files1, txt_files2

def convert_all_txt_to_csv():
    txt_files1, txt_files2 = get_txt_files()
    all_txt_files = txt_files1 + txt_files2
    headers = get_column_headers_from_xls() 

    for txt_path in all_txt_files:
        try:
            df = read_flexible_txt(txt_path)
            if df.empty:
                print(f"⚠️ Archivo vacío o ilegible: {txt_path}")
                continue

            if "Leaderboard_Submission" not in txt_path:
                df.columns = headers[:df.shape[1]]

            csv_path = txt_path.replace(".txt", ".csv")
            df.to_csv(csv_path, index=False)
            print(f"{os.path.basename(txt_path)} → columnas detectadas: {df.shape[1]}")

            os.remove(txt_path)
            print(f"✅ Convertido y eliminado: {txt_path} → {csv_path}")

        except Exception as e:
            print(f"❌ Error procesando {txt_path}: {e}")

    print("Todos los archivos .txt han sido convertidos y eliminados.")
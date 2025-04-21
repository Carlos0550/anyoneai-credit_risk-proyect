import pandas as pd

def read_flexible_txt(txt_path: str) -> pd.DataFrame:
    rows = []
    try:
        with open(txt_path, "r", encoding="latin1", errors="replace") as f:
            for line in f:
                fields = line.strip().split()
                rows.append(fields)
        return pd.DataFrame(rows)
    except Exception as e:
        print(f"⚠️ Error leyendo manualmente {txt_path}: {e}")
        return pd.DataFrame()  # Por si hay errores
import os
local_downloads_folder = os.path.join(os.getcwd(), "datasets")

def start_extract_files():
    extracted_folder = os.path.join(os.getcwd(), "datasets", "extracted")
    os.makedirs(extracted_folder, exist_ok=True) 

    for filename in os.listdir(local_downloads_folder):
        if filename.endswith(".zip"):
            print(f"Extrayendo {filename}")
            zip_path = os.path.join(local_downloads_folder, filename)
            os.system(f'unzip -o "{zip_path}" -d "{extracted_folder}"')  
            os.remove(os.path.join(local_downloads_folder, filename))
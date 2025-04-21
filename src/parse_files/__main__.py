from xls_analyzer import analyze_xls_file
from file_utils import convert_all_txt_to_csv
from time import sleep
import os

if __name__ == "__main__":
    analyze_xls_file()
    sleep(10)
    os.system("clear")
    sleep(1)
    convert_all_txt_to_csv()
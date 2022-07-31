from pathlib import Path
import re,csv 

file_path_1 = Path.cwd()/"csv_reports"/"pfb_overheads.csv"
print(file_path_1.exists())

with file_path_1.open(mode = "r", encoding = "UTF-8") as file:
    for line in file.readlines():
        print(line)



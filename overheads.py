from pathlib import Path
import re, csv

file_path_3 = Path.cwd()/"csv_reports"/"Overheads.csv"
print(file_path_3.exists())

with file_path_3.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
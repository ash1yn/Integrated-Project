from pathlib import Path
import re, csv

file_path_1 = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
print(file_path_1.exists())

with file_path_1.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
from pathlib import Path
import re, csv

overheads = Path.cwd()/"csv_reports"/"Overheads.csv"
print(overheads.exists())

with overheads.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(line)
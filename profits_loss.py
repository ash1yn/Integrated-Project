from pathlib import Path
import re, csv

profits_loss = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
print(profits_loss.exists())

with profits_loss.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
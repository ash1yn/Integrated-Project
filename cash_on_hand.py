from pathlib import Path
import re, csv
from api import convertUSDtoSGD

cash_on_hand = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
print(cash_on_hand.exists())

with cash_on_hand.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
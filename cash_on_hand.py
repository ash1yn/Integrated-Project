from pathlib import Path
import re, csv

cash_on_hand = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
print(cash_on_hand.exists())

cash = []
day = []
with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next (reader)
    for line in reader:
        print(line)
        day.append(int(line[0]))
        cash.append(int(line[1]))
    
    for coh in range(day, cash):



print(cash)
    
        
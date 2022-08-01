from pathlib import Path
import re, csv
import string
from api import convertUSDtoSGD

cash_on_hand = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
print(cash_on_hand.exists())

cash = []
day = []
with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next (reader)
    for line in reader:
        print(line)
        day.append(float(line[0]))
        cash.append(float(line[1]))

    for value in range (day, cash):
        if cash[value] < cash[value-1]:
            print(f"*Day: {day(value)}, Value Difference: {cash[value-1]-cash[value]}*")
        else:
            print("Cash on hand for each period is higher than the previous period")



        
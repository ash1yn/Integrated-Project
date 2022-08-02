from pathlib import Path
from pickle import FALSE, TRUE
import re, csv
from api import convertUSDtoSGD

cash_on_hand = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
print(cash_on_hand.exists())

day_cash_list = []
with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next (reader)
    for line in reader:
        day_cash_list.append([int(line[0]), int(line[1])])

    last_index = len(day_cash_list)-1

    all_higher = TRUE

    for i in range(last_index):
        if day_cash_list[i][1] > day_cash_list[i+1][1]:
            print(f"* DAY: {day_cash_list[i+1][0]}, AMOUNT: SGD {convertUSDtoSGD(day_cash_list[i][1]-day_cash_list[i+1][1])} *")
            all_higher = FALSE
        
    if all_higher == TRUE:
        print("Cash on hand for each period is higher than the previous period")

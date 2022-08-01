from pathlib import Path
from pickle import FALSE, TRUE
import re, csv
from api import convertUSDtoSGD

profits_loss = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
print(profits_loss.exists())

day_profit_list = []

with profits_loss.open(mode = "r", encoding = "UTF-8") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line)
        day_profit_list.append([int(line[0]),int(line[4])])

    last_index = len(day_profit_list)-1

    all_higher = TRUE

    for i in range(last_index):
        if day_profit_list[i][1] > day_profit_list[i+1][1]:
            print(f"* DAY: {day_profit_list[i+1][0]}, AMOUNT: SGD {convertUSDtoSGD(day_profit_list[i][1]-day_profit_list[i+1][1])} *")
            all_higher = FALSE

    if all_higher == TRUE:
        print("Net Profit for each period is higher than the previous period")
    

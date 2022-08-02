from pathlib import Path
from pickle import FALSE, TRUE
import re, csv
from api import convertUSDtoSGD

profits_loss = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
# Create a file path to the "Profit and Loss.csv" file in the "csv_reports" folder
print(profits_loss.exists())

day_profit_list = []
# Create an empty list to append

with profits_loss.open(mode = "r", encoding = "UTF-8") as file:
# Opens the "Profits and Loss.csv" file in read mode
    reader = csv.reader(file)
    # Reads the file
    next(reader)
    # Skips the header
    for line in reader:
        day_profit_list.append([int(line[0]),int(line[4])])
        # Appends the day and net profit values, found in the "Profit and Loss.csv" into the empty list (in a nested list format)

    last_index = len(day_profit_list)-1

    all_higher = TRUE

    for i in range(last_index):
        if day_profit_list[i][1] > day_profit_list[i+1][1]:
        # If the net profit value is not consecutively higher each day, 
            print(f"* DAY: {day_profit_list[i+1][0]}, AMOUNT: SGD {convertUSDtoSGD(day_profit_list[i][1]-day_profit_list[i+1][1])} *")
            # The day where net profit is lower than the previous day and the value difference in SGD, will be highlighted
            all_higher = FALSE

    if all_higher == TRUE:
    # If net profit value is consecutively higher each day,
        print("Net Profit for each period is higher than the previous period")
    

from pathlib import Path
from pickle import FALSE, TRUE
import re, csv
from api import convertUSDtoSGD

cash_on_hand = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
# Create a file path to the "Cash on Hand.csv" file in the "csv_reports" folder
print(cash_on_hand.exists())

day_cash_list = []
# Create an empty list to append
with cash_on_hand.open(mode = "r", encoding = "UTF-8", newline = "") as file:
# Open the "Cash on Hand.csv" file in read mode
    reader = csv.reader(file)
    # Reads the "Cash on Hand.csv" file
    next (reader)
    # Skips the header
    for line in reader:
        day_cash_list.append([int(line[0]), int(line[1])])
        # Appends the day and cash on hand values, found in the "Cash on Hand.csv" into the empty list (in a nested list format)

    last_index = len(day_cash_list)-1

    all_higher = TRUE

    for i in range(last_index):
        if day_cash_list[i][1] > day_cash_list[i+1][1]:
        # If the cash on hand value is not consecutively higher each day (all_higher = FALSE)
            print(f"* DAY: {day_cash_list[i+1][0]}, AMOUNT: SGD {convertUSDtoSGD(day_cash_list[i][1]-day_cash_list[i+1][1])} *")
            # The day where cash on hand is lower than the previous day, and the value difference in SGD, will be highlighted
            all_higher = FALSE
        
    if all_higher == TRUE:
    # If cash on hand value is consecutively higher each day
        print("Cash on hand for each period is higher than the previous period")
        
